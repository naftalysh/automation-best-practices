# System Design Interview Series

## Core Topics

### Scalability and Performance
- **Load Balancing**: Distributing incoming network traffic across multiple servers to ensure no single server bears too much load.
  - [Load Balancing](https://www.nginx.com/resources/glossary/load-balancing/)

- **Caching Strategies**: Temporary storage of copies of data to reduce access time and improve performance.
  - [Caching Overview](https://www.cloudflare.com/learning/cdn/what-is-caching/)

- **Database Sharding and Partitioning**: Splitting a large database into smaller, more manageable pieces.
  - [Database Sharding](https://www.digitalocean.com/community/tutorials/understanding-database-sharding)

- **Replication**: Copying and maintaining database objects in multiple databases.
  - [Database Replication](https://aws.amazon.com/what-is/database-replication/)

### Data Storage
- **SQL vs. NoSQL Databases**: Different types of databases designed for different purposes.
  - [SQL vs. NoSQL](https://www.mongodb.com/nosql-explained/nosql-vs-sql)

- **Data Consistency, Availability, and Partition Tolerance (CAP Theorem)**: Trade-offs between different aspects of a distributed database system.
  - [CAP Theorem](https://www.ibm.com/cloud/learn/cap-theorem)

- **Indexing and Query Optimization**: Techniques to improve the performance of database queries.
  - [Database Indexing](https://use-the-index-luke.com/sql/anatomy/the-tree)

- **Data Warehousing and Data Lakes**: Systems for storing large amounts of structured and unstructured data.
  - [Data Warehousing vs. Data Lakes](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/)

### Networking
- **HTTP/HTTPS Protocols**: Protocols for communication over the web.
  - [HTTP/HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP)

- **WebSockets and Real-Time Communication**: Protocols for interactive communication between a client and a server.
  - [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

- **DNS and CDN**: Systems for translating domain names and distributing content.
  - [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
  - [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)

- **Network Partitioning and Fault Tolerance**: Designing systems to handle network failures.
  - [Network Partitioning](https://en.wikipedia.org/wiki/Partition_tolerance)

### System Architecture
- **Monolithic vs. Microservices Architecture**: Different approaches to building software applications.
  - [Monolithic vs. Microservices](https://microservices.io/patterns/monolithic.html)

- **Service-Oriented Architecture (SOA)**: A design pattern where services are provided to other components by application components.
  - [SOA](https://searchapparchitecture.techtarget.com/definition/service-oriented-architecture-SOA)

- **Event-Driven Architecture**: A design pattern in which decoupled applications can asynchronously publish and subscribe to events.
  - [Event-Driven Architecture](https://aws.amazon.com/event-driven-architecture/)

- **Design Patterns**: Common solutions to recurring design problems.
  - [Design Patterns](https://refactoring.guru/design-patterns/)

### Security
- **Authentication and Authorization**: Verifying identity and granting access to resources.
  - [Authentication vs. Authorization](https://auth0.com/intro-to-iam/authentication-vs-authorization)

- **Data Encryption (In-Transit and At-Rest)**: Protecting data by encoding it.
  - [Data Encryption](https://www.ibm.com/cloud/learn/data-encryption)

- **OAuth, JWT, and Other Token-Based Systems**: Protocols for secure authentication.
  - [OAuth](https://oauth.net/)
  - [JWT](https://jwt.io/introduction/)

- **Secure Coding Practices**: Techniques to prevent security vulnerabilities.
  - [Secure Coding](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)

### Distributed Systems
- **Consensus Algorithms (e.g., Paxos, Raft)**: Algorithms for achieving agreement among distributed processes.
  - [Consensus Algorithms](https://raft.github.io/)

- **Distributed File Systems (e.g., HDFS)**: Systems for storing and managing files across multiple machines.
  - [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)

- **Message Queues and Pub/Sub Systems (e.g., Kafka, RabbitMQ)**: Systems for managing and distributing messages.
  - [Kafka](https://kafka.apache.org/intro)
  - [RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

- **MapReduce and Distributed Computing Frameworks**: Techniques for processing large data sets with a distributed algorithm.
  - [MapReduce](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

### APIs and Integration
- **RESTful APIs vs. GraphQL**: Different approaches to designing web APIs.
  - [RESTful APIs](https://restfulapi.net/)
  - [GraphQL](https://graphql.org/learn/)

- **API Rate Limiting and Throttling**: Techniques to control the amount of incoming and outgoing traffic to and from a network.
  - [API Rate Limiting](https://www.3scale.net/api-rate-limiting/)

- **API Versioning**: Strategies to manage changes in API versions.
  - [API Versioning](https://www.freecodecamp.org/news/api-versioning-explained-with-example-65a52f226d3a/)

- **Middleware and API Gateways**: Software that provides common services and capabilities for applications.
  - [Middleware](https://en.wikipedia.org/wiki/Middleware)
  - [API Gateways](https://www.nginx.com/products/api-gateway/)

## Approach to System Design

### Requirement Gathering
- **Understanding Functional and Non-Functional Requirements**: Identifying the needs and constraints of the system.
  - [Requirements Gathering](https://www.jamasoftware.com/blog/what-is-requirements-gathering/)

- **Clarifying Assumptions and Constraints**: Ensuring a clear understanding of the system's limitations.
  - [Assumptions and Constraints](https://project-management.info/project-assumptions/)

### High-Level Design
- **Define Major System Components and Interactions**: Outline the main parts of the system and how they interact.
  - [High-Level Design](https://www.tutorialspoint.com/software_engineering/software_design_basics.htm)

- **Create a High-Level Architecture Diagram**: Visual representation of the system’s architecture.
  - [Architecture Diagrams](https://www.visual-paradigm.com/guide/enterprise-architecture/what-is-an-architecture-diagram/)

### Detailed Design
- **Dive into the Specifics of Each Component**: Detailed description of the system’s components.
  - [Detailed Design](https://en.wikipedia.org/wiki/Software_design_description)

- **Design Database Schemas, API Endpoints, and Service Interactions**: Define the structure and interactions within the system.
  - [Database Schema Design](https://www.databasestar.com/database-schema/)
  - [API Design](https://swagger.io/resources/articles/best-practices-in-api-design/)

### Scalability Considerations
- **Identify Potential Bottlenecks**: Recognize areas that may limit system performance.
  - [Identifying Bottlenecks](https://stackify.com/what-is-application-bottleneck/)

- **Plan for Horizontal and Vertical Scaling**: Strategies to expand system capacity.
  - [Scaling](https://aws.amazon.com/elasticloadbalancing/features/scaling/)

### Fault Tolerance and Recovery
- **Design for Redundancy and Failover Mechanisms**: Ensure system reliability and continuous operation.
  - [Fault Tolerance](https://www.redhat.com/en/topics/automation/what-is-fault-tolerance)

- **Implement Monitoring and Alerting**: Tools and techniques to detect and respond to system issues.
  - [Monitoring and Alerting](https://aws.amazon.com/devops/monitoring/)

### Performance Optimization
- **Use Caching Effectively**: Improve system performance by storing frequently accessed data.
  - [Effective Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

- **Optimize Database Queries and Indexing**: Enhance the performance of database operations.
  - [Query Optimization](https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/basic-search)

## Recommended Resources

### Books
- **"Designing Data-Intensive Applications" by Martin Kleppmann**
  - [Free Preview](https://dataintensive.net/)
- **"Site Reliability Engineering" by Google**
  - [Free Online Version](https://sre.google/sre-book/table-of-contents/)
- **"System Design Interview" by Alex Xu**
  - [Book Website](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF)

### Online Courses
- **Coursera's "Scalable Web Applications" Course**
  - [Course Link](https://www.coursera.org/learn/scalable-web-apps)
- **Udacity's "Designing Data-Intensive Applications" Course**
  - [Course Link](https://www.udacity.com/course/data-engineer-nanodegree--nd027)

### Practice Platforms
- **Grokking the System Design Interview on Educative.io**
  - [Course Link](https://www.educative.io/courses/grokking-the-system-design-interview)
- **LeetCode's System Design Problems**
  - [LeetCode](https://leetcode.com/problemset/all/?topicSlugs=system-design)

### Community and Forums
- **Reddit’s r/sysadmin and r/askengineers**
  - [r/sysadmin](https://www.reddit.com/r/sysadmin/)
  - [r/askengineers](https://www.reddit.com/r/askengineers/)
- **Stack Overflow and SystemDesignPrimer GitHub Repository**
  - [Stack Overflow](https://stackoverflow.com/)
  - [SystemDesignPrimer](https://github.com/donnemartin/system-design-primer)
