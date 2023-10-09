"What time it is!?"
#pause
Start-Sleep -seconds 5
"That's right! It's " + (get-date).ToString('T') + "!"


#$location = [System.TimeZoneInfo]::Local | Select-Object -expandproperty Id
#if ($location -match "Eastern") {$x = " EST"}
#if ($location -match "Pacific") {$x = " PST"}
#if ($location -match "Central") {$x = " CST"}
#"Time: " + (get-date).ToString('T') + $x

##Code sourced from StackOverFlow and Microsoft PowerTips
##Citations in description on GitHub