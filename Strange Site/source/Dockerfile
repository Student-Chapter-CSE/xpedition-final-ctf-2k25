# Use the official Go image as a build stage
FROM golang:1.24.1-alpine3.21 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Go module file if it exists
COPY go.mod ./

# Download dependencies if go.mod is present
RUN if [ -f "go.mod" ]; then go mod download; fi

# Copy the source code
COPY . .

# Build the Go application
RUN go build -o server

# Use a minimal base image for the final container
FROM alpine:3.21

# Install necessary dependencies
RUN apk --no-cache add ca-certificates

# Set the working directory
WORKDIR /app

# Copy the compiled binary from the builder stage
COPY --from=builder /app/server .

# Copy static files and templates
COPY templates/ templates/

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["./server"]
