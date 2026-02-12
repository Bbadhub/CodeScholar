# Ambience

**Ambience is an operating system designed for deploying IoT microservices efficiently across various hardware platforms.**

**Category:** operating_system  
**Maturity:** proven (widely used in production)

## How It Works

Ambience provides abstractions for deploying microservices with strongly typed interfaces. It allows for flexible deployment by determining isolation boundaries at deployment time and using asynchronous computational models. The system optimizes performance through zero-copy inter-process communication (IPC) and remote procedure calls (RPC) for service communication.

## Algorithm

**Input:** Deployment manifests written in a Domain Specific Language (DSL) embedded in Python, defining services, dependencies, and network configurations.

**Output:** Custom kernel images for each node that instantiate the specified microservices and their configurations.

**Steps:**

1. 1. Define microservices with strongly typed interfaces using an interface definition language (IDL).
2. 2. Create deployment manifests that specify service dependencies, network topologies, and security isolation groups.
3. 3. Compile custom kernel images for each target node based on the deployment manifest.
4. 4. Assign microservices to groups for shared address space or isolation based on deployment requirements.
5. 5. Utilize zero-copy IPC for communication within groups and RPC for communication between groups.

**Core Operation:** `output = custom_kernel_images(deployment_manifest)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `service_instance` | {name: 'detection', service: tf_lite_detection} | Defines the specific microservice to be deployed. |
| `network` | {udp-internet: 4898} | Specifies the network configuration for the microservices. |
| `group` | {name: 'camera_group', services: ['detection', 'camera']} | Determines how microservices are grouped for shared address space or isolation. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Ambience is designed for high efficiency in IoT applications, achieving significant performance improvements over traditional operating systems.

## Implementation

```python
def deploy_microservices(manifest: str) -> str:
    # Step 1: Parse the deployment manifest
    services = parse_manifest(manifest)
    # Step 2: Compile kernel images for each node
    kernel_images = compile_kernels(services)
    # Step 3: Assign services to groups
    assign_to_groups(services)
    # Step 4: Return the custom kernel images
    return kernel_images
```

## Common Mistakes

- Neglecting to define strong types for service interfaces, leading to runtime errors.
- Failing to specify all dependencies in the deployment manifest, causing deployment failures.
- Overlooking the need for security isolation in service groups.

## Use When

- Building IoT applications that require efficient resource management across heterogeneous devices.
- Developing microservices that need to be deployed on both low-resource microcontrollers and high-performance servers.
- Needing a flexible isolation model for microservices that can adapt at deployment time.

## Avoid When

- Developing applications that require POSIX compatibility.
- When a general-purpose operating system is needed for non-IoT applications.
- In scenarios where existing middleware solutions are sufficient.

## Tradeoffs

**Strengths:**

- High efficiency in resource utilization across diverse hardware.
- Flexible deployment and isolation models for microservices.
- Significantly improved throughput and lower latency compared to traditional OS.

**Weaknesses:**

- Limited applicability outside of IoT environments.
- Not suitable for applications requiring POSIX compliance.
- Complexity in defining deployment manifests and service interfaces.

**Compared To:**

- **vs Linux operating system:** Use Ambience for IoT-specific applications requiring high efficiency; use Linux for general-purpose applications.
- **vs Azure IoT platform:** Ambience offers better performance for specific IoT tasks, while Azure provides broader cloud integration.

## Connects To

- Microservices architecture
- Domain Specific Languages (DSL)
- Zero-copy IPC mechanisms
- Remote Procedure Calls (RPC)

## Evidence (Papers)

- **Ambience: an operating system for IoT microservices** [3 citations] - [DOI](https://doi.org/10.55056/jec.786)
