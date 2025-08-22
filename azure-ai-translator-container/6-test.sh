#!/bin/bash

echo "=> Status check"
curl http://localhost:5000/status
# OK Response
# {"service":"texttranslation","apiStatus":"NonMetered","apiStatusMessage":"Container is non-metered and does not require an API Key."}

echo
echo "=> Readiness check"
curl http://localhost:5000/ready
# OK Response
# {"service":"texttranslation","ready":"ready","message":"Container is non-metered and does not require an API Key."}

echo
echo "=> Translate pdf"
curl -i -X POST \
  "http://localhost:5000/translator/document:translate?api-version=2024-05-01&sourceLanguage=en&targetLanguage=zh-Hant" \
  -F "document=@sample.pdf;type=application/pdf" \
  -o "sample_translated.pdf"

echo "=> Translate Markdown"
curl -i -X POST \
  "http://localhost:5000/translator/document:translate?api-version=2024-05-01&sourceLanguage=en&targetLanguage=zh-Hant" \
  -F "document=@sample.md;type=text/markdown" \
  -o "sample_translated.md"

echo
ls -lt sample_translated.*

echo
echo "=> Disconnected Usage check"
curl http://localhost:5000/records/usage-logs
