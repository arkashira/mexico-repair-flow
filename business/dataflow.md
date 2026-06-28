 # Dataflow Architecture for Mexico Repair Flow

This dataflow architecture outlines the system design for the Mexico Repair Flow, a digital quoting and workflow management tool tailored to Mexican auto repair shops. The architecture aims to streamline processes, improve customer experience, and address the specific pain points of Mexican auto repair shops.

## External Data Sources
- **Mexican Auto Repair Shops**: Data collected from various sources such as APIs, web scraping, or direct integration with shop management systems.
- **Third-Party Parts Suppliers**: Data on parts pricing, availability, and delivery times.
- **Customer Data**: Customer information, vehicle details, and repair history.

## Ingestion Layer
- **API Gateway**: Handles incoming requests from various sources, enforces authentication, and routes them to the appropriate services.
- **Data Ingestion Services**: Responsible for parsing, cleaning, and validating data from external sources before passing it to the processing layer.

## Processing/Transform Layer
- **Quoting Service**: Generates digital quotes based on the collected data, considering parts pricing, labor costs, and shop rates.
- **Workflow Management Service**: Manages the repair workflow, assigning tasks, tracking progress, and notifying relevant parties.
- **Machine Learning Service**: Utilizes machine learning models to predict repair times, identify potential issues, and optimize repair processes.

## Storage Tier
- **Relational Database**: Stores structured data such as customer information, repair history, and parts pricing.
- **NoSQL Database**: Stores unstructured data such as images, videos, and customer feedback.
- **Data Lake**: Stores raw, unprocessed data for future analysis and machine learning model training.

## Query/Serving Layer
- **API Services**: Exposes the functionality of the various services to the external world, ensuring a consistent and secure interface.
- **Real-Time Analytics**: Provides real-time insights into repair shop performance, customer satisfaction, and parts usage.

## Egress to User
- **Mobile App**: Allows repair shop employees and customers to interact with the system, view quotes, track repairs, and provide feedback.
- **Web Portal**: Provides a web-based interface for repair shop employees to manage their workflows and access system data.

## Auth Boundaries
- **OAuth 2.0**: Used for authentication and authorization of users and third-party services.
- **JWT**: Used for secure token-based authentication within the system.