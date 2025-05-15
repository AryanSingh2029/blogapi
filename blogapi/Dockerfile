# Use an official OpenJDK image
FROM openjdk:17-jdk-slim

# Set the working directory
WORKDIR /app

# Copy everything to the container
COPY . .

# Build the application
RUN ./mvnw clean install

# Expose the port Spring Boot runs on
EXPOSE 8080

# Run the application
CMD ["java", "-jar", "target/blogapi-0.0.1-SNAPSHOT.jar"]
