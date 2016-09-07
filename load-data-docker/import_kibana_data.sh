es_response=$(curl -s --w "%{http_code}" -o /dev/null -X POST $1/_bulk -u elastic:changeme --data-binary "@kibana.json" -H "Expect:")
if [ 0 -eq $? ] && [ $es_response = "200" ]; then
echo "Loading default indexes...OK"
fi
