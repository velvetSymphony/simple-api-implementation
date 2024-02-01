# Simple API creation using python

- This is just a sample/simple implementation of an API created using the python ```http.server``` module.
- I did not want to use django/flask for my API implementations as I was more interested in how it was implemented with just native python.
- Refer to [these docs here](https://docs.python.org/3/library/http.server.html#module-http.server) to learn more about ```http.server```.

## Implementation

- Simply clone this repo, and run ```python api_server.py```.
- This should start a local server using port 8080.
- To make requests, simply use cURL.
    - I've deliberately used non-standard method definitions here (only for ```GET```, ```POST``` is still the same.)to just play around.

### Retrieve

- Equivalent of ```GET```.
- ```curl -X RETRIEVE 'http://localhost:8080/hello/name' -v```
- Returns the following message:
-   ```json
    {"Name": "velvets"}
    ```

### POST

- ```curl -X POST 'http://localhost:8080/posty' -H "Content-Length: 18" -d '{"Reason": "4fun"}'```
- Returns the payload data back. In this case
-   ```json
    {"Reason": "4fun"}
    ```
- This payload data passed is then written to a text file ```payload_data.txt```. I was too lazy to put a DB behind.

### Future

- Might be adding some more stuff in the future just to experiment.
- That's it, enjoy :-)
