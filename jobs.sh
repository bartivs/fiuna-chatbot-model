#!/etc/bin/bash
echo "START EXPORT OF EVENTS ${date}"
TABLE_OR_SELECT="events" 
LOCAL_FILE=/app/dumps/events.csv 
psql -U $POSTGRES_USER -h db -p 5432 -d rasa -c "COPY $TABLE_OR_SELECT TO stdout CSV HEADER DELIMITER ','  quote '\"' force quote *"  > $LOCAL_FILE
echo "END EXPORT OF EVENTS ${date}"