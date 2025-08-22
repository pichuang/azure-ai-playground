
The diagram below shows a hub-spoke network architecture. We want the hub VM (vm-hub-taiwannorth) inside the hub to be able to connect to the spoke VM (vm-spoke-taiwannorth) inside the spoke through the Azure Firewall (azfw-taiwannorth)on the same VNet. In this situation, how should we define the UDR in the Azure route table to make sure symetric routing?


Purpose
Environment
2 * Azure Virtual Network
{10.100.254.0/24, 10.100.255.0/24} vnet-hub-taiwannorth
10.100.254.0/28 snet-hub-vm-taiwannorth
10.100.255.192/26 AzureFirewallSubnet
10.100.100.0/24 vnet-spoke-taiwannorth
10.100.100.0/29 snet-spoke-vm-taiwannorth
2 * Azure Route Table
rt-hub
rt-spoke
3 * Necessary IP infomations
10.100.254.4 vm-hub-taiwannorth
10.100.255.196 azfw-taiwannorth
10.100.100.4 vm-spoke-taiwannorth
Problem: After setting up route, the traffic still does not go through Azure Firewall
If you are very familiar with Azure Network Hub-Spoke Topology, you should be very familiar with the following routing configuration if you want to force all 0.0.0.0/0 traffic to go through Azure Firewall


incorrect udr design
After you set it up this way, you will find that vm-hub-taiwannorth and vm-spoke-taiwannorth still do not communcate through the Azure Firewall

Root Cause: VNet Peering has default routes
The key lies in Azure Traffic Routing > Sysmte Routes > Default

Azure virtual network traffic routing
Learn how Azure routes virtual network traffic and how you can customize routing for Azure.

Azure Docs
yujiang111

If there are routes from VNet Peering, it will become like this:

Source	Address prefixed	Next hop type
Default	Unique to the virtual network	Virtual Network
Default	0.0.0.0/0	Internet
Default	Unique from Virtual Network Peering Address Space	VNet Peering
According to the rules above, let's go back and look at the effctive routes of these 2 VMs, as shown below:

From the perspective of vm-hub-taiwannorth, view effective routes:


incorrect-vm-hub-taiwannorth
From the perspective of vm-spoke-taiwannorth, view effective routes:


incorrect-vm-spoke-taiwannorth
As with most network routers, routing decisions are primarily based on Longest Prefix Match (LPM), so /24 prefix takes precedence over /0.


So... when the source IP of vm-hub-taiwannorth is 10.100.255.4 and the desination IP of vm-spoke-taiwannorth is 10.100.100.4, it will NOT route according to the default route 0.0.0.0/0 you hvae set. Instead, it will first use the directly connected Default system route 10.100.100.0/24 to reach the destination IP.

Solution: Add More Specific Routes
Add a route for the desitnation address prefix to prevent the default route of VNet Peering from taking precedence over 0.0.0.0/0.


solution
Add New Route for Hub role
Add a new route, 10.100.100.0/24 NH 10.100.255.196, to override the default route 10.100.100.0/24 NH VNet Peering


correct-route-table-vm-hub-taiwannorth
From the perspective of vm-hub-taiwannorth, view effective routes:


correct-vm-hub-taiwannorth
You will see that the defaulr route status of 10.100.100.0/24 has become Invalid from Active, and it has been replaced by the route we wrote ourselves.

Add New Route for Spoke role
Add a new route, 10.100.254.0/28 NH 10.100.255.196, to ensure that traffic to vm-hub-taiwannorth (10.100.254.4) passws through Azure Firewall.


correct-route-table-vm-spoke-taiwannorth
From the perspective of vm-spoke-taiwannorth, view effective routes:


correct-vm-spoke-taiwannorth
NOTE: You need to clearly know the subnet range (10.100.254.0/28) when vm-hub-taiwannorth is located, rather than directly entering the entire Hub VNet range (10.100.254.0/23). Doing so will cause vm-spoke-taiwannorth to be unable to route to the Azure Firewall Service if they are all placed under the same address prefix.

You May Need to Know
ALWAYS REMEMBER Longest Prefix Match (LPM)
Longest prefix match - Wikipedia

Wikimedia Foundation, Inc.
Contributors to Wikimedia projects

Remember to power on the Azure VM: By default, the Effective routes on the network interface card will ONLY have content after the Azure VM is powered on. if the Azure VM is not powered on, there will be no Effective Routes information generated.