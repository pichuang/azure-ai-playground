# 衛生福利部醫療領域資通系統資安防護基準

## 一、依據

衛生福利部(以下簡稱本部)為資通安全管理法醫療領域特定非公務機關
之中央目的事業主管機關,就該特定領域類型資通系統有另為規定防護
基準之必要,爰依資通安全責任等級分級辦法第11條第2項後段規定,訂
定本防護基準,供醫院資通系統實施各項資安防護控制措施之依循。

## 二、適用範圍

本防護基準適用範圍為依資通安全管理法受本部轄管之醫療領域之特定
非公務機關。

醫療儀器資通系統與其他支援設施資通系統應依循機關之資安維護計
畫,涉及相關組織及委外管理等要項,須依循機關之資安管理框架。

## 三、用詞定義:

(一)資安列管醫療儀器:指放置院區內場域,有對外連線網際網路
(Internet)或連結院內系統網路(Intranet),或具網路位址(IP)
追蹤性,或交換資料間接上傳醫療相關資訊系統(如:PACS、HIS)等
之臨床使用醫療終端儀器及控制系統。

(二)醫療資訊系統(Healthcare Information System, HIS):指傳統醫療
資訊業務管轄之臨床資訊應用系統,包含資料庫及後端處理臨床表
單之系統。

(三)醫療影像儲傳系統(Picture archiving and communication
system,PACS):包含OT之影像擷取組像及上傳元件端與IT之醫療
影像傳輸儲存及調閱系統端二部份;元件端,為具醫療數位影像傳
輸協定(DICOM Module)醫療儀器的集合,系統端,含醫師醫囑項目
與照攝影像及報告資訊。

(四)醫療儀器資通系統:泛指資安列管醫療儀器之控制系統分群、終端
儀器分群之邊界主機,參考「醫療儀器資安分群分類模型」範圍。

(五)醫療物聯網裝置(The Internet of Medical Things, IoMT):泛指
藉由物聯網(The Internet of Things,IoT)技術進行資料蒐集或傳
輸之設備。

(六)邊界主機:指管理獨立網域內網(Local LAN)運作之儀器群組主機,
並隔離介接院內系統網路(Intranet)之具網路區隔功能閘道器或伺
服主機(如:雙網卡Edge Gateway 或 Device Server)。

(七)儀器獨立網域內網(Local LAN):指儀器群組(為:「群組型儀器」
或「系統型儀器」)依儀器原廠建議或工控區(OT Zone)資安防護目
的,所規劃及佈建的獨立網域內網,以確保穩定性、安全性需求;
或稱「設備內網」、「內內網」。

(八)儀器獨立網段:指院內系統網路(Intranet)網域,分割隔離網段
後,規劃獨立於行政電腦網段外,專屬予醫療儀器運行使 $A$
段。

(九)OT防火牆:對比於資通區(IT Zone)介接網際網路(Internet)的「醫
院外部防火牆」名詞,指醫院內部「資安列管類醫療儀器」分區佈
建後,介接院內系統網路(Intranet)的醫療儀器跨區防火牆。

## 四、醫療儀器資安分群分類

(一)機關盤點具連網功能的醫療儀器資產,應涵蓋「資安列管醫療儀
器」之範圍。

(二)「資安列管醫療儀器」依「元件」與「系統」資料流之從屬關係特
性,作為「分群」依循,為「終端儀器」與「控制系統」二群;依
資料流來源至目的IP之跨區軌跡,作為「分類」依循,二群分五類
(如附圖一);透過「醫療儀器資安分群分類模型」模型化分群分
類,防護標的實施普、中、高分級的控制措施項目。

(三)終端儀器群:指臨床上使用之醫療儀器,經連結院內系統網路
(Intranet)傳輸資料之儀器設備或醫療儀器,包含三類:「終端單
機」、「群組型儀器」及「系統型儀器」。

1\. 終端單機:指臨床使用直接連結院內系統網路(Intranet)傳輸資
料至資通區(IT Zone)中繼邊界 Gateway 之單機型醫療儀器。如:
超音波影像儀為單機型醫療儀器,傳輸資料連結PACS 系統之工作
清單 Gateway、DICOM 影像 Gateway。

2\. 群組型儀器:指多台功能相同之醫療儀器組成獨立網域內網
(Local LAN),透過隔離措施間接進行單機院內系統網路
(Intranet)連線之「內網邊界主機」。如:ICU生理監視器群組的

中央站、內網化連網洗腎機群組的邊界主機(Edge Loader
Gateway) ·

3\. 系統型儀器:指由不同功能模組單機在獨立網域內網(Local LAN)
組合而成一套醫療儀器,透過隔離措施間接進行單機院內系統網
路(Intranet)連線之內網邊界主機;或指使用於臨床獨立網域內
網(Local LAN),多台功能不相同模組單機組合而成一套醫療儀器
的「邊界主機」,經隔離間接連結院內系統網路(Intranet)。
如:MRI、CT、PET連結PACS 系統的介面控制台 console。

(四)控制系統群:指規格上可連線管理2台(含)以上「終端儀器」群之
終端單機或邊界主機,連結院內系統網路(Intranet)傳輸資料之臨
床儀器控制系統,包含「醫儀控制系統」與「醫儀應用系統」二
類。

1\. 醫儀控制系統:全稱為「醫療儀器資訊控制系統」,指控制「終
端儀器」非人類連線的管理系統(Device Server);只管理「儀器
ID」及「檢驗檢查資料」;不落地儲存與醫療相關資訊系統交換
的「可識別資料」、不管理資料查詢的「醫事人員帳密權控」;
功能上不涉及識別個人資訊的控制軟體系統。如:ICU生理監護系
統伺服器主機、洗腎機拋轉系統設備伺服器的控制軟體系統。

2\. 醫儀應用系統:全稱為「醫療儀器資訊應用系統」,指「終端儀
器」的控制應用管理系統(AP Server);包含交換且儲存HIS病人
個資資訊、提供臨床人員查詢報告等服務,有管理醫事人員帳密
權控等可識別資訊的儀器控制及連結臨床應用套裝軟體系統。
如:產房資訊系統、檢驗備管系統伺服器的應用軟體系統。

## 五、機關資通系統適用規定

(一)機關自行或委外開發之資通系統,應依「資通安全責任等級分級辦
法」第11條附表九所定資通系統防護需求分級原則完成資通系統分
級,並依附表十所定資通系統防護基準執行控制措施。

$$\quad \quad ;$$
「資安列

(二)醫療儀器應符合「醫療器材管理法」及相關子法與「醫療器材品質
管醫療儀器」終端儀器群邊界主機與控制系統群為醫療儀器資通系
統防護基準之防護標的,應依本防護基準附表一執行控制措施。

(三)其他支援設施之特定類型資通系統,執行「資通安全責任等級分級
辦法」第11條附表十所定控制措施,因技術限制、系統設計、結構
或性質等因素,就特定事項或控制措施之辦理或執行顯有困難者,
得參考其他領域公告之相關資通或工控系統之控制措施。

## 六、醫療儀器資料流管理

(一)「資安列管醫療儀器」分群分類之醫療儀器,依資安風險區劃 ZCR
方法,評估分區「防護需求等級(SL)」、規劃「網路安全區塊
(Zone)」分區、建立跨區資料傳輸「安全管道(Conduit)」;ZCR 網
路規劃參考公用之醫療儀器資料流網路模板(Template)。(如附圖
二)

(二)資安風險區劃(Zone, conduit and risk assessment, ZCR):「資安
列管醫療儀器」分群分類之醫療資料流,依評估資安需求等級
SL(Security Level)規劃建立「網路安全區塊(Zone)」分區;跨區
管道(Conduit)佈建資料流通道之過濾阻擋「控制項」防護機制,達
到:受攻擊面縮小(Attack Surface Reduction)、縱深防禦
(Defense in Depth)等防護效果之資安風險管理實作流程。

(三)資安防護需求等級(Security Level, SL):針對「控制系統」依據資
通系統防護需求分級原則,評估機密性(C)、完整性(I)、可用性
(A)、法遵性(L)各構面之分級取最高等級者,評估「資產價值」,
評定普、中、高之「資安防護需求等級」,簡稱SL(Security
Level);SL由低至高分級為SL(0)~SL(4)對應資安防護需求普、
中、高等級。

1\. SL(0):指「信任連線」。

2\. SL(1)~ SL(2):資安防護需求等級普級。

3\. SL(3)為:資安防護需求等級中級。

4\. SL(4)為:資安防護需求等級高級。

(四)信任連線:指經風險評鑑後,風險可承受範圍內的短距離機器連線
資料傳輸;對應防護需求等級為SL(0);安全(Safety)議題另受醫療
法規「醫療器材管理法」規範。

(五)網路安全區塊(Zone):指「資安列管醫療儀器」之建置,網路規劃
上的資料流資安防護需求分區,可分「網際網路(Internet)」、
「院內系統網路(Intranet)」、「工控區(OT Zone)」、「信任連
線」區塊(包含:儀器獨立網域內網(Local LAN)、RS232連線、藍
芽、RF、IR…等低風險短距連線)。每一區塊,透過資安風險評估資
安防護需求等級(SL),每一資安風險區塊(Zone)內之資安列管儀器
列為相同SL;「子區塊」之SL≤「母區塊」。

(六)管道(Conduit):泛指跨「網路安全區塊(Zone)」之間,經套用對應
跨區等級「控制項」防護機制(如:資料流經隔離、清洗、阻擋)

$$,$$
$$\quad \quad \quad \quad$$
。

(一)本防護基準「醫療儀器資料流網路模版」,提供機關確認「終端儀
器群」與「控制系統群」之醫療資訊資料流、清查連網方式、連網
儀器及所介接系統,依分區完成資安風險評估,並執行對應控制措
施。

$$\left( \right)$$

在套用「控制措施」後,依據可能發生的外部事件影響風險構面,
每年針對「資安列管儀器」,經選擇適用規範之「風險識別」、
「風險分析」與「衝擊分析」等風險評估工具與方法論,逐年檢討
「資安風險等級(Cyber Risk Level,CRL)」之低、中、高等級,改
善資安風險。

1\. $: \pi$ 。

2\. 中:可能接受的(Potentially Acceptable)。

3\. 低:可接受的(Acceptable)。

## 八、實作指引

為協助機關落實本防護基準,逐年完備機關之醫療儀器資安防護控制措
施,由本部另行公告「醫療儀器資通系統資安防護作業實作指引」,供
醫院導入實務運作參考。

<table>
<caption>附表一 醫療儀器資通系統資安防護基準</caption>
<tr>
<th colspan="2">控制項</th>
<th></th>
<th>系統防護需求分級</th>
<th colspan="2">資安列管醫療儀器 $5$ 護標的</th>
</tr>
<tr>
<th>控制 構面</th>
<th>控制 目標</th>
<th>分級</th>
<th>控制措施</th>
<th>終端儀器 群之邊界 主機</th>
<th>控制系統 群</th>
</tr>
<tr>
<td rowspan="5">網路 架構</td>
<td rowspan="3">網段規劃</td>
<td>高</td>
<td>一、規劃院內OT防火牆,並有對應控制系統之網路管控措 施(如:網路封包過濾功能、支援之工控協定等)。 二、等級「中」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>中</td>
<td>一、規劃儀器獨立網段網路與院內系統網路區隔,並有跨 區(Zone)院內 OT 防火牆連網政策規則。 二、等級「普」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>一、「群組型儀器」、「系統型儀器」,應適當區域內網 化規劃。 二 、 在 「 院 內 系 統 網 路 」 與 「 儀 器 獨 立 網 域 內 網 」 網 絡 跨 區(Zone)架設院內 OT 防火牆或採取風險控制補償 措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">邊界防護</td>
<td>高 中</td>
<td>一 、 監 視 「 控 制 系 統 」 外 部 邊 界 與 關 鍵 內 部 邊 界 之 通 訊 。 二 、 等 級 「 普 」 之 所 有 控 制 措 施 。</td>
<td></td>
<td>◼ ☒</td>
</tr>
<tr>
<td>$\frac { 3 1 6 } { 5 }$</td>
<td>「邊界主機」、「控制系統」網絡「邊界主機」應採 取防護具體措施,並定期審查防護措施。</td>
<td>◼ ☒</td>
<td>◼ ☒</td>
</tr>
<tr>
<td rowspan="4">$1 7$ 控制</td>
<td rowspan="3">帳號管理</td>
<td>高</td>
<td>一、定期盤點帳號並審核,並有相關異常管理機制。 二、等級「中」之所有控制措施。</td>
<td></td>
<td>◼ ☒</td>
</tr>
<tr>
<td>中</td>
<td>一、已不被授權(如:離職或調任)之帳號予以刪除或停 用。 二、帳號定期變更密碼。 三、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { 3 1 6 } { 5 2 }$</td>
<td>一、「終端儀器」有原廠預設帳密應變更預設密碼,如無 法更改應有其他補償措施。 二、「控制系統」工作站/伺服器作業系統應變更原廠預設 帳號密碼;儀器原廠無法變更者,應有資安管理作業 程序。 三、「控制系統」非合法權控帳號定期點檢。 四、「醫儀應用系統」依循醫院規定之帳號管理機制,且 不得使用共用帳號。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>遠端存取</td>
<td>高中 $\frac { x } { 8 }$</td>
<td>一、應依循醫院規定遠端存取管理規範,包含連線需求申 請、使用限制與使用者權限檢查等作業並留存記錄。 二、醫院遠端存取,應有時效性限制及「院內系統網路 (Intranet)」監控機制。</td>
<td>◼</td>
<td>◼</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">控制項</th>
<th></th>
<th>系統防護需求分級</th>
<th colspan="2">資安列管醫療儀器 防護標的</th>
</tr>
<tr>
<th>控制 構面</th>
<th>控制 目標</th>
<th>分級</th>
<th>控制措施</th>
<th>終端儀器 $=$ $\pm$</th>
<th>控制系統 群</th>
</tr>
<tr>
<td rowspan="3"></td>
<td>最小權限</td>
<td>$\frac { 7 } { 1 9 }$ 中 $\frac { x } { 8 }$</td>
<td>臨床使用者開機權限應採最小權限原則,僅開放使用者必 要之授權存取及應用;儀器原廠無法變更者,應有其他 補償措施。</td>
<td>◼ ☒</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">無線網路 管理</td>
<td>高 中</td>
<td>一、「資安列管醫療儀器」及「IoMT」依特性及使用目 ☐ 的,分網路安全區塊(Zone)設置Wi-Fi 無線網路熱點 (SSID),配置對等之資安防護措施以連線「院內系統 網路(Intranet)」 二、等級「普」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>一、「資安列管醫療儀器」及「IOMT」的使用,其Wi-Fi 無線網路建立相關區隔網段與存取權限授權,應依循 網 管 理 規 二 、 限 制 Wi-Fi 無 線 連 網 儀 器 和 院 內 核 心 網 路 之 間 的 資 料 交換。 三、實作「儀器獨立網域內網(Local LAN)」Wi-Fi 無線網 路熱點(SSID)安全機制。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="9">事件日 誌與可 歸責性</td>
<td rowspan="2">事件記錄</td>
<td>高 中</td>
<td>一、應定期審查所保留產生之日誌,並保留日誌至少六個 月,如無日誌紀錄供審查應有其他補償措施。 二、等級「普」之所有控制措施</td>
<td></td>
<td>◼ ☒</td>
</tr>
<tr>
<td></td>
<td>有 適 當 之 日 誌 紀 錄 , 如 無 法 留 存 日 誌 紀 錄 應 有 其 他 補 償 措 「邊界主機」、「醫儀控制系統」、「醫儀應用系統」,留 施。</td>
<td>◼ ☒</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">日誌紀錄 內容</td>
<td>高 中</td>
<td>一、確保日誌紀錄格式至少應包含發生事件、發生時間、 使用者等追蹤資訊。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { i n } { B }$</td>
<td>系統日誌紀錄功能內容應有明確記錄欄位資訊,如無結構紀 錄應有其他補償措施。</td>
<td>◼ ☒</td>
<td>◼ ☒</td>
</tr>
<tr>
<td>日誌儲存 容量</td>
<td>$\frac { v } { 1 2 }$ 中 $\frac { i f t } { B }$</td>
<td>配置適當日誌紀錄的儲存容量。</td>
<td>☒ ◼</td>
<td>☒ ◼</td>
</tr>
<tr>
<td>日誌處理 失效之回 應</td>
<td>高中 $\frac { i n } { 5 }$</td>
<td>日誌處理失效時應採取適當之行動。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">時戳</td>
<td>高 中</td>
<td>一 、 系 統 內 部 時 鐘 應 定 期 與 基 準 時 間 源 進 行 同 步 。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>☒ ◼</td>
</tr>
<tr>
<td>普</td>
<td>時間定期(手/自動)校時或同步機制。</td>
<td>☒ ◼</td>
<td>☒ ◼</td>
</tr>
<tr>
<td>日誌資訊 之保護</td>
<td>高 中</td>
<td>一 、 日 誌 紀 錄 有 備 份 保 存 管 理 機 制 。 二 、 等 級 「 普 」 之 所 有 控 制 措 施 。</td>
<td></td>
<td>☒ ◼</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">控制項</th>
<th></th>
<th>系統防護需求分級</th>
<th colspan="2">資安列管醫療儀器 防護標的</th>
</tr>
<tr>
<th>控制 構面</th>
<th>控制 目標</th>
<th>分級</th>
<th>控制措施</th>
<th>終端儀器 $=$ $\pm$</th>
<th>控制系統 群</th>
</tr>
<tr>
<td></td>
<td></td>
<td>$\frac { 3 1 6 } { 5 2 }$</td>
<td>日誌紀錄有存取權限管理,對日誌之存取僅限於有權限之使 用人員,以防護日誌資訊之完整性。</td>
<td>◼ ☒</td>
<td>◼ ☒</td>
</tr>
<tr>
<td rowspan="6">$\frac { 1 } { 3 }$ 續 $\frac { 1 } { 5 } + \frac { 3 } { 1 2 }$</td>
<td rowspan="2">營運持續 $\frac { 1 } { 6 } + \frac { 3 } { 1 2 }$</td>
<td>高 中</td>
<td>一、應有系統備份機制並確認備份完整性且有備份復原機 制。 二、等級「普」之所有控制措施。 ☐</td>
<td></td>
<td>◼ ☒</td>
</tr>
<tr>
<td>$\frac { x } { 8 }$</td>
<td>一、臨床使用應訂有臨床業務營運持續計畫,於可容忍時 間內替代流程提供服務,並執行演練。 二、定期審查營運持續計畫,以維持臨床服務之可用性與 病人安全。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">安全模式</td>
<td>高 中</td>
<td>一、「醫儀控制系統」、「醫儀應用系統」系統安全模式 操作,可以自動或手動啟動,如危及安全時有手動或 自動暫時替代 bypass 功能。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼ ☒</td>
</tr>
<tr>
<td>$\frac { i \pi } { 5 }$</td>
<td>一、「資安列管醫療儀器」依循醫院限制或防止入侵者存 取的安全機制(如:封鎖單機IP或暫時離線機制)。 二、「終端儀器」可離線單機運作。</td>
<td>◼ ☒</td>
<td>◼ ☒</td>
</tr>
<tr>
<td rowspan="2">控制系統 備援</td>
<td>高 中</td>
<td>一 、 具 有 進 階 備 援 機 制 。 二 、 等 級 「 普 」 之 所 有 控 制 措 施 。</td>
<td></td>
<td>◼ ☒</td>
</tr>
<tr>
<td>$\frac { i n } { 5 }$</td>
<td>「邊界主機」、「控制系統」之儀器伺服器主機具有持續營 運機制。</td>
<td>◼ ☒</td>
<td>◼ ☒</td>
</tr>
<tr>
<td rowspan="5">識別與 鑑別</td>
<td>內部使用 $\frac { 1 } { 4 } \geq \frac { 3 } { 6 }$ 與鑑別</td>
<td>高中 $\frac { i n } { 5 }$</td>
<td>依循醫院帳號及權控管理機制建立內部一般使用者、最高管 理者及廠商等帳號管理;如無法單一識別使用者時,須有替 代監管措施,如排班表、影像紀錄等。</td>
<td></td>
<td>☒ ◼</td>
</tr>
<tr>
<td rowspan="2">裝置之識 別與鑑別</td>
<td>高 中</td>
<td>一、「醫儀控制系統」與「醫儀應用系統」應識別與鑑別 ☐ 連接至系統之「終端儀器」,及擁有終端儀器管理機 制,如無法識別與鑑別連接之「終端儀器」應有其他 ☐ 補償措施。 二、等級「普」之所有控制措施。 ☐</td>
<td>◼ ☒</td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>連結「院內系統網路」儀器,應依循醫院申請審核流程與網 ☐ 管 IP配發作業規範。</td>
<td>☒ ◼</td>
<td>☒ ◼</td>
</tr>
<tr>
<td>身分鑑別 管理</td>
<td>高中 $\frac { x } { 8 }$</td>
<td>一、應有帳戶識別機制,如無法單一使用者鑑別時,須有 替代管理措施,如使用者值排、排班紀錄等鑑別使用 者。 二、「醫儀應用系統」身分驗證應依循醫院帳號管理規則 ☐ (如:納入醫院單一登錄系統);若系統無法依循醫院 帳號管理規則,須有其他補償管理措施。</td>
<td>☒ ◼</td>
<td>◼</td>
</tr>
<tr>
<td>鑑別資訊</td>
<td>$\frac { v } { 1 0 }$</td>
<td>應遮蔽在鑑別過程 $\quad$ 。</td>
<td>☒ ◼</td>
<td>☒ ◼</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">控制項</th>
<th></th>
<th>系統防護需求分級</th>
<th colspan="2">資安列管醫療儀器 防護標的</th>
</tr>
<tr>
<th>控制 構面</th>
<th>控制 目標</th>
<th>分級</th>
<th>控制措施</th>
<th>終端儀器 $=$ $\pm$</th>
<th>控制系統 群</th>
</tr>
<tr>
<td></td>
<td>回饋</td>
<td>中 $\frac { i n } { 5 }$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="3">系統與 通訊防 護</td>
<td rowspan="2">傳輸之機 密性與完 整性</td>
<td>高 中</td>
<td>二 、 院 內 OT 防 火 牆 只 開 啟 儀 器 需 使 用 之 網 路 通 訊 服 務 埠 。 一、設定院內OT防火牆只允許儀器跨區(Zone)傳輸資料之 伺服器、工作站、合法傳輸點IP之白名單路由。 三、等級「普」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>連線「院內系統網路(Intranet)」終端儀器邊界主機或控 制系統伺服器主機,應有邏輯隔離或實體隔離,如無法邏 輯隔離或實體隔離應有其他補償措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>資料儲存 之安全</td>
<td>$\frac { 1 } { 1 2 }$ 中 $\frac { 3 1 6 } { 8 }$</td>
<td>系統、應用程式組態備份靜置資訊之儲存媒體裝置,應予以 防護。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="3">系統與 服務獲 得</td>
<td rowspan="2">外部系統 服務</td>
<td>高 中</td>
<td>一、外部之服務供應商(Service Provider)、系統整合商 (System Integrator)應提供系統資安證明文件(如: 第三方安全性檢測證明),涉及使用非自行開發之系統 或資源者,應標示非自行開發之內容與其來源及授權 證明。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>「邊界主機」、「控制系統」之供應商(Product Supplier)、系統整合商(System Integrator)或服務供應商 (Service Provider)所提供之外部系統服務,應將資安要求 納入醫院制式契約並要求服務供應商確實遵守。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>$\quad$</td>
<td>高 中 $\frac { i n } { 5 }$</td>
<td>定期審查資訊安全管理系統相關文件、更新紀錄;存檔管理 醫療儀器相關驗收文件。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="4">實體與 環境防 護</td>
<td>實體(儀器 使用者)存 取授權</td>
<td>高中 $\frac { x } { 8 }$</td>
<td>置放場域相關使用者授權應審查符合醫院醫療照護相關規範 (如:醫院評鑑),進出置放場域須有授權人員管控(如:配 戴證件、分組班表、動線出入口 CCTV),變更時亦同。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="3">實體(儀器 門禁)進出 控制</td>
<td>高</td>
<td>一、伺服器主機應有獨立機房及環控設施,如:設置於中 央資訊機房。 二、等級「中」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>中</td>
<td>一、設施所在區域有實體隔離機制,置放場域經授權人員 進出管理與紀錄(如:授權人員門禁刷卡紀錄)。 二、等級「普」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>置放場域應符合醫院醫療照護相關環境安全規範(如:醫院 評鑑),置放場域需有授權人員進出管制機制。</td>
<td>◼</td>
<td>◼</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">控制項</th>
<th></th>
<th>系統防護需求分級</th>
<th colspan="2">資安列管醫療儀器 防護標的</th>
</tr>
<tr>
<th>控制 構面</th>
<th>控制 目標</th>
<th>分級</th>
<th>控制措施</th>
<th>終端儀器 $=$ $\pm$</th>
<th>控制系統 群</th>
</tr>
<tr>
<td rowspan="6"></td>
<td rowspan="2">緊急電源</td>
<td>高 中</td>
<td>一、即時替代電力供應,系統儀器主機應有專用或中央不 斷電UPS供電。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>長 時 間 緊 急 發 電 電 力 備 援 機 制 , 符 合 醫 院 醫 療 照 護 相 關 環 境 「邊界主機」、「控制系統」建立能供應最小業務負載量之 安全規範(如:醫院評鑑),並有定期公共安全查檢。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>實體公用 服務備援</td>
<td>高 中 | $\frac { 3 6 } { 8 }$</td>
<td>調 、 消 防 及 通 訊 等 環 境 動 力 源 ) 應 有 備 援 機 制 , 並 依 循 定 期 「資安列管醫療儀器」置放場域公用服務(如水、氣、空 公共安全查檢。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>實體危害 因素控制</td>
<td>高中普</td>
<td>一、置放場域之環境應依循醫院危害因素控制管理規範, 符合儀器規格之危害因素防護要求(依原廠規範,如: 對於溫溼度控制、水損、火、煙、水、震動、化學效 應、電力供應、電磁、輻射或人為入侵破壞等危害因 素)。 二、置放場域之環境應依循醫院危害因素控制管理規範與 定期公共安全查檢,並符合「原子能法」、「游離輻 射防護法」輻防管制法令規範。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">第三方/陪 同者的存 $H$</td>
<td>高 中</td>
<td>一、「醫儀控制系統」與「醫儀應用系統」非醫院人員存 取,須有院方人員陪同與記錄機制。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { i n } { 5 }$</td>
<td>「邊界主機」、「控制系統」置放場域非醫院人員存取應依 循醫院人員實體存取安全控制管理規範,包含人員進出管 理、可攜式行動資訊設備存取管理與其他有關醫院資安要 求。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="3">系統與 $\pi$ 整性</td>
<td rowspan="3">漏洞修補</td>
<td>高</td>
<td>一、針對具資安風險之漏洞或軟體,在儀器原廠許可下, 對具資安風險之漏洞進行修補或軟體更新,並完成測 試,或採取補償性控制措施來避免資安風險。 二、針對終端儀器邊界主機及控制系統伺服器,每年排程 弱點掃描。 三、等級「中」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>中</td>
<td>一、加強醫療儀器外部資安情資蒐集分析與因應控制措 施。 二、等級「普」之所有控制措施。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { i \pi } { 5 }$</td>
<td>在儀器原廠許可下,針對具資安風險之漏洞或軟體更新,或 採取補償性控制措施,以降低資安風險。</td>
<td>◼</td>
<td>◼</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">控制項</th>
<th></th>
<th>系統防護需求分級</th>
<th colspan="2">資安列管醫療儀器 防護標的</th>
</tr>
<tr>
<th>控制 構面</th>
<th>控制 目標</th>
<th>分級</th>
<th>控制措施</th>
<th>終端儀器 $=$ $\pm$</th>
<th>控制系統 群</th>
</tr>
<tr>
<td rowspan="7"></td>
<td rowspan="2">惡意程式 防護</td>
<td>$\frac { \frac { 1 } { 1 2 } } { 1 2 }$ 中</td>
<td>一、控制系統應有偵惡意程式防護機制,如無法佈署惡意 防護工具應有其他型式對策(如:加強USB 惡意程式掃 描等)或採取補償性控制措施來避免資安風險。 二、控制系統應納入全院 Intranet 網路安全監控機制,並 有警訊通報或回饋機制;如無法納入全院網路安全監 控應有其他補償措施。 三、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>普</td>
<td>應實作降低弱點暴露應因應對策,控制系統或儀器主機應在 儀器原廠許可下安裝防毒軟體,如無法佈署惡意防護工具應 有其他補償措施(如:醫院內部OT防火牆對應控制系統之防 護政策等)。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>系統監控</td>
<td>高 中 |</td>
<td>監 控 工 具 在 不 影 響 控 制 系 統 操 作 可 用 性 下 , 納 入 「 院 內 系 統 具 ); 如 無 法 納 入 應 有 其 他 補 償 措 施 。 網路」系統監控回饋機制(如:SOC、SIEM 等 IT資安監控工</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">可預測之 故障預防</td>
<td>高 中</td>
<td>一、建立故障預防機制,分析系統可靠度與潛在故障因素 (如平均故障時間、故障原因分析等),及早因應。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { i \pi } { 5 }$</td>
<td>建立系統維護紀錄管理機制,並符合醫院醫療照護相關環境 安全規範(如醫院評鑑),包含定期維護、檢查、測試、保養 或校正作業,並有紀錄可查。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="2">故障容許 度</td>
<td>高 中</td>
<td>一、評估重要組件容錯機制(如:終端設備斷線儲存/連線 重傳機制、使用隔離抗干擾網路線材、昇級安全通訊 協定等),提升控制系統資安韌性,進行防護措施,如 無法評估或經評估無法提供防護應有適當措施。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { i n } { B }$</td>
<td>遵循「醫療器材管理法」法令規範建立通報機制,ADR不良 品及不良反應通報系統通報回饋製造商以持續改善產品。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td rowspan="3">組態 $\frac { A 5 } { B }$ 理</td>
<td rowspan="2">組態變更 控制</td>
<td>$\frac { v } { 1 2 }$ 中</td>
<td>一、建立組態變更管理機制(如:變更申請流程、維修工 單作業紀錄文件化)。 二、等級「普」之所有控制措施。</td>
<td></td>
<td>◼</td>
</tr>
<tr>
<td>$\frac { i n } { B }$</td>
<td>一、系統初始安裝期間,若設定非原廠之預設功能組態 時,應有組態還原機制(如:組態設定紀錄、組態備 份)。 二、系統營運期間組態變更時,應文件化保留變更紀錄。</td>
<td>◼</td>
<td>◼</td>
</tr>
<tr>
<td>最基本功 能</td>
<td>高中 $\frac { i n } { 5 }$</td>
<td>依儀器原廠手冊安裝程序組態設定,系統設定時,僅提供業 務必要的最小功能(如:關閉連外瀏覽器、只可安裝原廠已 授權之第三方軟體)。</td>
<td>◼</td>
<td>◼</td>
</tr>
</table>

註:防護需求控制措施防護需求說明及實務操作指引,可參考「醫療儀器資

$$\quad \quad \quad$$

附圖一、醫療儀器資安分群分類模型

醫療儀器資安分群分類模型

資安列管醫療儀器

<figure>

終 $\nexists _ { \mathrm { I I I } } ^ { \mathrm { L L } }$ 儀器群

控制系統群

終端單機

群組型儀器

系統型儀器

醫儀資訊控制
系統

醫儀資訊應用
系統

</figure>

一、「資安列管醫療儀器」依「元件」與「系統」特性,分為「終端儀器」
與「控制系統」二群。

二、「終端儀器」群包含三類:「終端單機」、「群組型儀器」、「系統型
儀器」。

三、「控制系統」群包含二類:「醫療儀器資訊控制系統類」、「醫療儀器
資訊應用系統類」。

## 附圖二、醫療儀器資料流網路模板

<figure>
<figcaption>【醫療儀器資訊網路基本架構圖公用參考範例】</figcaption>

醫療儀器資料流網路模板

批價

資材

企業區(Enterprise Zone)

申報

經營管理
會計

人資

Conduit

資通區(IT Zone)

醫療資通系統

HIS

LIS

護囑系統
NIS

PACS
儲存調
閱

EMR

醫囑系統

CIS

臨床表單

CDSS

院方交換Table

臨床 人機存取介面(HMI) (傳統程式 或 網頁程式)

$D e v i c e \quad s e r v e r + H L 7 \# S Q L \quad G a t e w a y$

$S L \left( n \right)$

企業資通系統

Conduit

Intranet 網管區(CT Zone)

Wifi 管理器

131111

((p))

控制系統群–醫儀控制系統

控制系統群–醫儀應用系統

醫療資通系統

Wifi 防火牆

0

Conduit

防火牆(如OT防火牆)

工控區(OT Zone)

SL(n)

終端儀器群

Device Server

SL1

Edge gateway

雙網卡(內外網)

SL1

信任連線(SLO)

Local LAN

RS232 / RS485/LPT/ USB / NFC/藍芽/紅外線

(SLO)

</figure>