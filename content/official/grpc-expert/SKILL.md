        ---
        name: grpc-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/grpc-expert/SKILL.md
        description: Design gRPC services with proto3 schemas, streaming, and error handling.
        ---

        You design production gRPC services with clean proto definitions.

## Proto Design
```protobuf
syntax = "proto3";

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
  rpc ListUsers (ListUsersRequest) returns (stream User);
  rpc CreateUser (CreateUserRequest) returns (User);
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
  google.protobuf.Timestamp created_at = 4;
}
```

## Error Handling
```go
// Return gRPC status codes, not panics
if user == nil {
    return nil, status.Errorf(codes.NotFound, "user %s not found", req.Id)
}
```

## Rules
- Use `google.protobuf.Timestamp` for all timestamps — not string or int64.
- Field numbers are forever — never reuse them even if you delete a field.
- Use server-side streaming for large result sets, not repeated unary calls.
- Define error details with `google.rpc.Status` for rich error info.
