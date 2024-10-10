# show PSAvoidUsingWriteHost
# show PSAvoidAssignmentToAutomaticVariable
function Get-CustomErrorMessage($ErrorMessage){ $Error = "Error occurred: $ErrorMessage" }

function Write-Test
{
	Write-Host "test"
}
