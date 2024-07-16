curl -i -X GET --http1.1 "localhost:9699/hitec/spellchecker/status" \
-H "Content-Type: application/json"

curl -i -X POST --http1.1 "localhost:9699/hitec/spellchecker/run" \
-H "Content-Type: application/json" \
--data-binary "@src/tests/komoot_reviews_1.json"
