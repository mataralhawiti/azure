# list all resource groups in current Subscription
$RG = Get-AzResourceGroup
$RG | Format-Table

# list all VMs in current Subscription
$VM = Get-AzVM
$VM | Format-Table


# list all VMs (just the name) across all my Subscriptions
$VMs = @()
$Sub = Get-AzSubscription
foreach($s in $Sub) {
    Get-AzSubscription -SubscriptionName $s.Name | Set-AzContext
    $VMs += Get-AzVM
}
$VMs.Name | Format-Table
