#!/bin/bash
echo "Waiting for MongoDB to start..."
sleep 100
echo "Initializing Replica Set..."
mongosh --host mongodb-0.mongodb-service:27017 <<EOF
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb-0.mongodb-service:27017" },
    { _id: 1, host: "mongodb-1.mongodb-service:27017" },
    { _id: 2, host: "mongodb-2.mongodb-service:27017" }
  ]
})
EOF
