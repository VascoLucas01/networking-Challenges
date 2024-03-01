#Script : PowershellADAutomation.ps1
#Purpose: Write a Powershell script that adds the below person to AD.
######### Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.
#Why    : 

[CmdletBinding()]
param (
    [string]$fullName=$null,

    [Parameter(Mandatory=-$True)]
    [string]$firstName,

    [Parameter(Mandatory=-$True)]
    [string]$lastName,

    [Parameter(Mandatory=-$True)]
    [string]$userLogon,

    [Parameter(Mandatory=-$True)]
    [string]$email,

    [Parameter(Mandatory=-$True)]
    [string]$jobTitle,

    [Parameter(Mandatory=-$True)]
    [string]$department,

    [Parameter(Mandatory=-$True)]
    [string]$company,

    [Parameter(Mandatory=-$True)]
    [string]$city,

    [Parameter(Mandatory=-$True)]
    [string]$office

)


### for the challenge itself
# $firstName  = Franz
# $lastName   = Ferdinand
# $userLogon  = Ferdinand
# $email      = ferdi@GlobeXpower.com
# $jobTitle   = TPS Reporting Lead
# $department = TPS
# $company    = GlobeX USA
# $city       = Springfield
# $office     = OR



Write-Verbose "Starting script..."
Write-Verbose "_______Person details_______"
Write-Verbose "Firt Name      : $firstName"
Write-Verbose "Last Name      : $lastName"
Write-Verbose "User logon name: $userLogon"
Write-Verbose "Email          : $email"
Write-Verbose "Job Title      : $jobTitle"
Write-Verbose "Department     : $department"
Write-Verbose "Company        : $company"
Write-Verbose "City           : $city"
Write-Verbose "Office         : $office"

if($fullName){
    New-ADUser -GivenName $firstName -Surname $lastName -Name
$fullName -SamAccountName $userLogon -EmailAddress $email -Title
$jobTitle -Department $department -Company $company -City $city
-Office $state
} else {
    $fullName = "$firstName $lastName"
    New-ADUser -GivenName $firstName -Surname $lastName -Name
$fullName -SamAccountName $userLogon -EmailAddress $email -Title
$jobTitle -Department $department -Company $company -City $city
-Office $state

}

Write-Verbose "Ending script..."
