# Use official OpenJDK image
FROM openjdk:17-jdk-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Give permission to mvnw
RUN chmod +x mvnw

# Build the app
RUN ./mvnw clean install

# Expose port
EXPOSE 8080

# Run the app
CMD ["java", "-jar", "target/*.jar"]
