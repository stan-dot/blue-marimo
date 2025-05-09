
# Architectural Decision Record: Pod File Sharing

## Context

In our Kubernetes-based system, we have a requirement to share dynamically generated files between two pods. The first pod processes and stores files, while the second pod consumes these files as Python modules. The file updates are triggered by user actions (e.g., button press), and the system should efficiently synchronize this data across the pods.

## Decision

We will use a **Persistent Volume Claim (PVC) with ReadWriteMany (RWX) access mode** for shared storage between the pods. This approach provides a straightforward, native file system interface, minimizing operational overhead and complexity.

## Options Considered

### **Option 1: Shared Persistent Volume (Recommended)**

**Pros:**

* Simple to set up and maintain.
* Provides native file system access, making Python module imports seamless.
* Low latency within the same cluster.
* Scales well within a single cluster.

**Cons:**

* Requires a backend storage solution that supports RWX (e.g., NFS, EFS, GlusterFS).
* May incur network latency depending on the storage type.

### **Option 2: S3 Bucket or Object Store**

**Pros:**

* Excellent for distributed, multi-cluster architectures.
* High durability and availability.
* Native versioning and lifecycle management.

**Cons:**

* Higher complexity for setup and integration.
* Increased latency due to network overhead.
* Requires explicit file synchronization logic.

### **Option 3: Kubernetes EmptyDir with rsync or Sidecar Sync**

**Pros:**

* Low latency.
* No external storage dependency.
* Simple, lightweight setup for ephemeral data.

**Cons:**

* Data is lost if the pod is restarted or rescheduled.
* Not suitable for persistent, shared state.

### **Option 4: REST API for File Syncing**

**Pros:**

* Fine-grained access control and extensibility.
* Easier to manage with mature API frameworks like FastAPI.

**Cons:**

* Overly complex for this use case.
* Higher code maintenance overhead.
* Requires additional serialization and deserialization logic.

## Decision Rationale

The **Persistent Volume Claim** approach offers the best balance of simplicity, performance, and flexibility for our current use case. It allows both pods to directly access shared files without requiring additional APIs or synchronization logic, making it the most efficient option for a single-cluster setup.

## Next Steps

* Set up the NFS server or appropriate RWX-compatible storage.
* Configure PVC and mount volumes in both pods.
* Implement health checks and capacity monitoring for the shared volume.

## Status

Accepted - Pending Implementation
