# Testing Leaf /fields endpoints

1. Will try the API first, to get a feeling of what it looks like.
   - Lost my API key. Where to reset it?
   - I can re-authenticate, ok.

2. Stored email and password in environment variables

3. Added pprint and formating to ease understanding of results.

4. Made a GET request to *https://api.withleaf.io/services/fields/api/fields*, result was:
    ```python
    [{'geometry': {'coordinates': [[[[-89.83466863632202, 39.726580599966866],
                                    [-89.83469009399414, 39.71951688444436],
                                    [-89.82966899871826, 39.71956639898719],
                                    [-89.8298192024231, 39.7278183260755],
                                    [-89.83466863632202, 39.726580599966866]]]],
                'type': 'MultiPolygon'},
    'id': 'c2b92626-fbd9-4a13-9297-e1fe8b8df9f2',
    'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
    'type': 'ORIGINAL'}]
    ```

5. Will try to do a POST request to the get endpoint. Result was:
    ```python
    {'detail': "Request method 'POST' not supported",
     'message': 'error.http.405',
     'path': '/api/fields',
     'status': 405,
     'title': 'Method Not Allowed',
     'type': 'https://www.jhipster.tech/problem/problem-with-message'}
    ```


6. Will try to do a POST request to *https://api.withleaf.io/services/fields/api/users/{leafUserId}/fields/*, without the id entry and without a package body:
   - Is there another way to get my leafUserId or is GET request the only way?
    Result was:
    ```python
    {'detail': 'Required request body is missing: public '
           'org.springframework.http.ResponseEntity<com.leaf.fields.web.rest.vm.FieldVm> '
           'com.leaf.fields.web.rest.FieldResource.createField(java.util.UUID,com.leaf.fields.web.rest.vm.FieldCriteria) '
           'throws java.lang.Exception',
     'message': 'error.http.400',
     'path': '/api/users/03fc1ab9-ea07-46d0-80e3-1d41ca70c222/fields/',
     'status': 400,
     'title': 'Bad Request',
     'type': 'https://www.jhipster.tech/problem/problem-with-message'}
    ```

7. Will try to do a POST request to *https://api.withleaf.io/services/fields/api/users/{leafUserId}/fields/*, without the id entry and with a package body in the following form:
    ```python
    {
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": [
            [
                [
                [-93.48821327980518, 41.77137549568163],
                [-93.48817333680519, 41.77143534378164],
                [-93.48821327390516, 41.76068857977987],
                [-93.48821327980518, 41.77137549568163]
                ]
            ]
            ]
        }
    }
    ```
    Result was:
    ```python
    {'geometry': {'coordinates': [[[[-93.48821327980518, 41.77137549568163],
                                [-93.48817333680519, 41.77143534378164],
                                [-93.48821327390516, 41.76068857977987],
                                [-93.48821327980518, 41.77137549568163]]]],
              'type': 'MultiPolygon'},
     'id': '1b20f36d-ad2d-4ba3-a05b-53d137cc54a9',
     'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
     'type': 'ORIGINAL'}
    ```

8. After repeating the POST request several times, noticed that I get a lot of fields with different ids but with the same coordinates on the GET request. Should't them be all merged? Just one of them is:
    ```python
    [{'geometry': {'coordinates': [[[[-93.48821327980518, 41.77137549568163],
                                    [-93.48817333680519, 41.77143534378164],
                                    [-93.48821327390516, 41.76068857977987],
                                    [-93.48821327980518, 41.77137549568163]]]],
                'type': 'MultiPolygon'},
     'id': 'b27f5bc3-0225-42dd-bc4a-efb1672cc015',
     'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
     'type': 'ORIGINAL'},
     {'geometry': {'coordinates': [[[[-93.48821327980518, 41.77137549568163],
                                     [-93.48817333680519, 41.77143534378164],
                                     [-93.48821327390516, 41.76068857977987],
                                     [-93.48821327980518, 41.77137549568163]]]],
                 'type': 'MultiPolygon'},
     'id': '73fc4bce-bccb-44d9-8c9a-517b9ffa3cd7',
     'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
     'type': 'MERGED'},
     {'geometry': {'coordinates': [[[[-93.48821327980518, 41.77137549568163],
                                     [-93.48817333680519, 41.77143534378164],
                                     [-93.48821327390516, 41.76068857977987],
                                     [-93.48821327980518, 41.77137549568163]]]],
                 'type': 'MultiPolygon'},
     'id': '1b20f36d-ad2d-4ba3-a05b-53d137cc54a9',
     'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
     'type': 'ORIGINAL'},
     {'geometry': {'coordinates': [[[[-89.83466863632202, 39.726580599966866],
                                     [-89.83469009399414, 39.71951688444436],
                                     [-89.82966899871826, 39.71956639898719],
                                     [-89.8298192024231, 39.7278183260755],
                                     [-89.83466863632202, 39.726580599966866]]]],
                 'type': 'MultiPolygon'},
     'id': 'c2b92626-fbd9-4a13-9297-e1fe8b8df9f2',
     'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
     'type': 'ORIGINAL'},
     {'geometry': {'coordinates': [[[[-93.48821327980518, 41.77137549568163],
                                     [-93.48817333680519, 41.77143534378164],
                                     [-93.48821327390516, 41.76068857977987],
                                     [-93.48821327980518, 41.77137549568163]]]],
                 'type': 'MultiPolygon'},
     'id': 'fa3f39a2-e97e-4bc4-9dde-96268d1367fa',
     'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
     'type': 'ORIGINAL'}]
    ```

9. I will better separate the functions to have a more readable codebase.
10. I propose pytest for unit/integration tests and locust for performance test. 
11. From now I will propose different combinations of request inputs on the GET and POST routes, in the way I think they should behave.
12. Apparently there is a field that cannot be erased:
    ```python
    {'geometry': {'coordinates': [[[[-89.83466863632202, 39.726580599966866],
                                    [-89.83469009399414, 39.71951688444436],
                                    [-89.82966899871826, 39.71956639898719],
                                    [-89.8298192024231, 39.7278183260755],
                                    [-89.83466863632202, 39.726580599966866]]]],
                'type': 'MultiPolygon'},
    'id': 'c2b92626-fbd9-4a13-9297-e1fe8b8df9f2',
    'leafUserId': '03fc1ab9-ea07-46d0-80e3-1d41ca70c222',
    'type': 'ORIGINAL'}
    ```
13. Filtering with *operationtype* returns fields that do not have *operationtype* set.

14. Deleting takes a lot of time
15. Different types of errors, like already existing fields and non closed fields, have the same status code (400):
    ```python
        <Response [400]>
        {'entityName': 'fieldsField',
        'errorKey': 'fieldAlreadyExists',
        'message': 'error.fieldAlreadyExists',
        'params': 'fieldsField',
        'status': 400,
        'title': 'You already have a field with id '
                'cc733c92-6853-45f6-8e49-bec741188ebb. Please, chose other id',
        'type': 'https://www.jhipster.tech/problem/problem-with-message'}
    ```
    ```python
        <Response [400]>
        {'detail': 'JSON parse error: Points of LinearRing do not form a closed '
                'linestring; nested exception is '
                'com.fasterxml.jackson.databind.JsonMappingException: Points of '
                'LinearRing do not form a closed linestring (through reference '
                'chain: com.leaf.fields.web.rest.vm.FieldCriteria["geometry"])',
        'message': 'error.http.400',
        'path': '/api/users/03fc1ab9-ea07-46d0-80e3-1d41ca70c222/fields/',
        'status': 400,
        'title': 'Bad Request',
        'type': 'https://www.jhipster.tech/problem/problem-with-message'}
    ```
16. There's some inconsistency on the error messages. While existing fields error has a errorKey, which is valuable for testing purposes, non-closed fields error does not return it.
17. I have created tests for the following scenarios:
    1.  Valid POST with valid coordinates, testing if the response matches the POST body
    2.  Invalid POST with non-closed coordinates, testing for error details
    3.  Invalid POST with intersecting coordinates (like an hourglass), testing for errorKey
    4.  Valid GET with existing userId, testing for the userId value (integration with POST)
    5.  Valid GET with unexisting userId, testing for empty fields list
    6.  Valid GET with existing field, testing for existence of field (integration with POST)