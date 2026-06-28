# tech-spec.md

## Stack

* Language: Node.js (14.x)
* Framework: Express.js (4.x)
* Runtime: Docker (20.x)
* Database: MongoDB (4.x) with Mongoose (6.x) ORM
* Frontend: React (17.x) with Webpack (5.x) bundler
* UI Library: Material-UI (5.x)
* Testing: Jest (27.x) with Enzyme (3.x)

## Hosting

* Primary Platform: AWS (free-tier-first)
* Secondary Platform: Google Cloud Platform (GCP)
* Containerization: Docker Hub with automated builds
* CI/CD: GitHub Actions with automated testing and deployment

## Data Model

### Tables/Collections

* **Repair Jobs** (`repairJobs` collection)
	+ `_id` (ObjectId): Unique identifier
	+ `customerName` (String): Customer name
	+ `vehicleMake` (String): Vehicle make
	+ `vehicleModel` (String): Vehicle model
	+ `repairDescription` (String): Repair description
	+ `estimatedCost` (Number): Estimated cost
	+ `status` (String): Status (e.g., "pending", "in-progress", "completed")
* **Work Orders** (`workOrders` collection)
	+ `_id` (ObjectId): Unique identifier
	+ `repairJobId` (ObjectId): Reference to Repair Jobs collection
	+ `workOrderDescription` (String): Work order description
	+ `estimatedTime` (Number): Estimated time
	+ `status` (String): Status (e.g., "pending", "in-progress", "completed")
* **Inventory** (`inventory` collection)
	+ `_id` (ObjectId): Unique identifier
	+ `partNumber` (String): Part number
	+ `partDescription` (String): Part description
	+ `quantity` (Number): Quantity
	+ `unitPrice` (Number): Unit price

## API Surface

### Endpoints

1. **GET /repair-jobs**: Retrieve a list of repair jobs
	* Method: GET
	* Path: `/repair-jobs`
	* Purpose: Retrieve a list of repair jobs
2. **POST /repair-jobs**: Create a new repair job
	* Method: POST
	* Path: `/repair-jobs`
	* Purpose: Create a new repair job
3. **GET /repair-jobs/{id}**: Retrieve a repair job by ID
	* Method: GET
	* Path: `/repair-jobs/{id}`
	* Purpose: Retrieve a repair job by ID
4. **PUT /repair-jobs/{id}**: Update a repair job
	* Method: PUT
	* Path: `/repair-jobs/{id}`
	* Purpose: Update a repair job
5. **DELETE /repair-jobs/{id}**: Delete a repair job
	* Method: DELETE
	* Path: `/repair-jobs/{id}`
	* Purpose: Delete a repair job
6. **GET /work-orders**: Retrieve a list of work orders
	* Method: GET
	* Path: `/work-orders`
	* Purpose: Retrieve a list of work orders
7. **POST /work-orders**: Create a new work order
	* Method: POST
	* Path: `/work-orders`
	* Purpose: Create a new work order
8. **GET /work-orders/{id}**: Retrieve a work order by ID
	* Method: GET
	* Path: `/work-orders/{id}`
	* Purpose: Retrieve a work order by ID
9. **PUT /work-orders/{id}**: Update a work order
	* Method: PUT
	* Path: `/work-orders/{id}`
	* Purpose: Update a work order
10. **DELETE /work-orders/{id}**: Delete a work order
	* Method: DELETE
	* Path: `/work-orders/{id}`
	* Purpose: Delete a work order

## Security Model

* Authentication: JSON Web Tokens (JWT) with refresh tokens
* Authorization: Role-based access control (RBAC) with MongoDB roles
* Secrets: Environment variables with Hashicorp Vault integration
* IAM: Google Cloud IAM with service accounts and roles

## Observability

* Logging: Morgan with Winston logger and MongoDB logging
* Metrics: Prometheus with Grafana dashboard
* Tracing: OpenTelemetry with Jaeger tracing

## Build/CI

* Build tool: Webpack with Babel transpilation
* CI tool: GitHub Actions with automated testing and deployment
* Testing framework: Jest with Enzyme and Mocha
* Code coverage: Istanbul with coverage reports