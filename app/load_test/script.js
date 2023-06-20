/*
 * REST Petclinic backend Api Documentation
 * This is REST API documentation of the Spring Petclinic backend. If authentication is enabled, when calling the APIs use admin/admin
 *
 * OpenAPI spec version: 1.0
 * Contact: vitaliy.fedoriv@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator.
 * https://github.com/OpenAPITools/openapi-generator
 *
 * OpenAPI generator version: 5.3.0
 */


import http from "k6/http";
import { group, check, sleep } from "k6";


const BASE_URL = "http://localhost:9966";
// Sleep duration between successive requests.
// You might want to edit the value of this variable or remove calls to the sleep function on the script.
const SLEEP_DURATION = 0.1;
// Global variables should be initialized.

export let options = {
    vus: 5000, // Virtual Users (concurrent users)
    duration: '30s', // Duration of the test
};

export default function () {
    group("/petclinic/error", () => {
        let url = BASE_URL + `/petclinic/error`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        request = http.put(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.post(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 4
        request = http.del(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 5
        request = http.patch(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 6
        request = http.head(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 7
        request = http.options(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 8
        request = http.trace(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/owners", () => {
        let lastName = 'Davis';
        let url = BASE_URL + `/petclinic/api/owners?lastName=${lastName}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Owner details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = {
            "address": "15th Av",
            "city": "New York",
            "firstName": "Lucas",
            "lastName": "Gonzales",
            "telephone": "3002587412"
        };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.post(url, body, params);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "The pet owner was sucessfully added.": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/owners/{ownerId}", () => {
        let ownerId = '8';
        let url = BASE_URL + `/petclinic/api/owners/${ownerId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Owner details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = {
            "address": "15th Av",
            "city": "New York",
            "firstName": "Lucas",
            "lastName": "Gonzales",
            "telephone": "3002587412"
        };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "Update successful.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.del(url);
        check(request, {
            "Owner details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/owners/{ownerId}/pets", () => {
        let ownerId = '3';
        let url = BASE_URL + `/petclinic/api/owners/${ownerId}/pets`;
        // Request No. 1
        let body = { "birthDate": "2022-05-27", "name": "Lucas", "type": { "id": "1", "name": "cat" } };
        let params = { headers: { "Content-Type": "application/json", "Accept": "application/json" } };
        let request = http.post(url, body, params);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "The pet was sucessfully added.": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/owners/{ownerId}/pets/{petId}", () => {
        let petId = '4'; // specify value as there is no example value for this parameter in OpenAPI spec
        let ownerId = '3'; // specify value as there is no example value for this parameter in OpenAPI spec
        let url = BASE_URL + `/petclinic/api/owners/${ownerId}/pets/${petId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Pet details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "birthDate": "2022-05-22", "name": "Lucas", "type": { "id": "1", "name": "cat" } };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        check(request, {
            "Update successful.": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/owners/{ownerId}/pets/{petId}/visits", () => {
        let petId = '4'; // specify value as there is no example value for this parameter in OpenAPI spec
        let ownerId = '3'; // specify value as there is no example value for this parameter in OpenAPI spec
        let url = BASE_URL + `/petclinic/api/owners/${ownerId}/pets/${petId}/visits`;
        // Request No. 1
        let body = { "date": "2022-06-24", "description": "The animal has lices" };
        let params = { headers: { "Content-Type": "application/json", "Accept": "application/json" } };
        let request = http.post(url, body, params);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "The vet visit was sucessfully added.": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/pets", () => {
        let url = BASE_URL + `/petclinic/api/pets`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Pet types found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "birthDate": "2022-05-23", "id": "4", "name": "Lucas", "ownerId": "3", "type": { "id": "1", "name": "cat" }, "visits": [] };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.post(url, body, params);
        check(request, {
            "Pet type created successfully.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/pets/{petId}", () => {
        let petId = '4'; // specify value as there is no example value for this parameter in OpenAPI spec
        let url = BASE_URL + `/petclinic/api/pets/${petId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Pet details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "birthDate": "2022-05-23", "id": "4", "name": "Lucas", "ownerId": "3", "type": { "id": "1", "name": "cat" }, "visits": [] };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "Pet details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.del(url);
        check(request, {
            "Pet details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/pettypes", () => {
        let url = BASE_URL + `/petclinic/api/pettypes`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Pet types found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "id": "7", "name": "horse" };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.post(url, body, params);
        check(request, {
            "Pet type created successfully.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/pettypes/{petTypeId}", () => {
        let petTypeId = '2'; // specify value as there is no example value for this parameter in OpenAPI spec
        let url = BASE_URL + `/petclinic/api/pettypes/${petTypeId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Pet type details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "id": "2", "name": "rat" };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "Pet type details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.del(url);
        check(request, {
            "Pet type details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/", () => {
        let url = BASE_URL + `/petclinic/`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        request = http.put(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.post(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 4
        request = http.del(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 5
        request = http.patch(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 6
        request = http.head(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 7
        request = http.options(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);

        // Request No. 8
        request = http.trace(url);
        check(request, {
            "OK": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/specialties", () => {
        let url = BASE_URL + `/petclinic/api/specialties`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Specialties found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "id": "4", "name": "cardiologist" };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.post(url, body, params);
        check(request, {
            "Specialty created successfully.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/specialties/{specialtyId}", () => {
        let specialtyId = '1';
        let url = BASE_URL + `/petclinic/api/specialties/${specialtyId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Specialty details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "id": "1", "name": "oncologist" };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "Specialty details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.del(url);
        check(request, {
            "Specialty details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/users", () => {
        let url = BASE_URL + `/petclinic/api/users`;
        // Request No. 1
        let body = { "enabled": "true", "password": "log#sa$d*/da", "roles": "admin", "username": "lucas27" };
        let params = { headers: { "Content-Type": "application/json", "Accept": "application/json" } };
        let request = http.post(url, body, params);
        check(request, {
            "User created successfully.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/vets", () => {
        let url = BASE_URL + `/petclinic/api/vets`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Vets found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = {
            "firstName": "Lucas",
            "id": "15",
            "lastName": "Gonzales",
            "specialties": {
                "name": "oncologist"
            }
        };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.post(url, body, params);
        check(request, {
            "Vet created successfully.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/vets/{vetId}", () => {
        let vetId = '1';
        let url = BASE_URL + `/petclinic/api/vets/${vetId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Vet details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = {
            "firstName": "James",
            "id": "1",
            "lastName": "Carter",
            "specialties": {
                "name": "oncologist"
            }
        };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "Pet type details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.del(url);
        check(request, {
            "Vet details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/visits", () => {
        let url = BASE_URL + `/petclinic/api/visits`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "visits found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "date": "2022-05-02", "description": "Free of lice", "id": "12", "petId": "4" };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.post(url, body, params);
        check(request, {
            "visit created successfully.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);
    });

    group("/petclinic/api/visits/{visitId}", () => {
        let visitId = '3';
        let url = BASE_URL + `/petclinic/api/visits/${visitId}`;
        // Request No. 1
        let request = http.get(url);
        check(request, {
            "Visit details found and returned.": (r) => r.status === 200
        });
        sleep(SLEEP_DURATION);

        // Request No. 2
        body = { "date": "2022-07-21", "description": "Free of lice", "id": "3", "petId": "8" };
        params = { headers: { "Content-Type": "application/json" } };
        request = http.put(url, body, params);
        check(request, {
            "Visit details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "Created": (r) => r.status === 201
        });
        sleep(SLEEP_DURATION);

        // Request No. 3
        request = http.del(url);
        check(request, {
            "Visit details found and returned.": (r) => r.status === 200
        });
        check(request, {
            "No Content": (r) => r.status === 204
        });
        sleep(SLEEP_DURATION);
    });
}