# Agentic Development Learning Plan

## Goal

Over 12 weeks, build and deploy a reliable AI research and task assistant that can:

- Understand a user's goal
- Plan multi-step work
- Select and use tools
- Connect to local and remote Model Context Protocol (MCP) servers
- Expose custom tools and resources through an MCP server
- Observe results and recover from errors
- Search documents and retain appropriate memory
- Request approval before consequential actions
- Produce a cited final result
- Be evaluated, monitored, and deployed

## Time commitment

- **Recommended pace:** 8–10 hours per week
- **Estimated total:** 112 hours
- **If you already know Python and APIs:** 6–8 hours per week
- **If programming is new to you:** 10–12 hours per week, possibly with two extra foundation weeks

### Suggested weekly routine

- Three weekday sessions of 60–75 minutes
- One weekend session of 4–5 hours
- Approximately 20% studying concepts
- Approximately 60% building and debugging
- Approximately 20% testing, reviewing, and documenting

## 12-week schedule

| Week | Focus | Hours | Deliverable |
|---|---|---:|---|
| 1 | Python fundamentals | 10 | Basic command-line task manager |
| 2 | APIs, JSON, files, and async Python | 10 | Task manager persisted to JSON and connected to an API |
| 3 | LLM application fundamentals | 7 | Model-powered command-line assistant |
| 4 | Tool calling | 9 | Assistant with at least three validated tools |
| 5 | Agent loop and MCP fundamentals | 10 | Multi-step agent and local MCP server |
| 6 | State, retrieval, and MCP integration | 10 | Document-aware agent using an MCP server |
| 7 | Long-term memory | 8 | Preference-aware agent |
| 8 | Planning and workflows | 9 | Structured research workflow |
| 9 | Evaluations and reliability | 10 | Automated agent and MCP evaluation suite |
| 10 | Agent framework, SDK, and production MCP | 8 | Framework-based agent using multiple MCP servers |
| 11 | Multi-agent patterns | 9 | Researcher, fact-checker, and writer system |
| 12 | Deployment | 12 | Usable web application or API |
| **Total** |  | **112** | **Deployed agent** |

## MCP progression

MCP is introduced only after direct tool calling so that the protocol does not hide the underlying agent mechanics.

```text
Week 4: Direct function tools
    ↓
Week 5: MCP architecture and a local server
    ↓
Week 6: Agent acting as an MCP client
    ↓
Week 9: MCP reliability and security evaluations
    ↓
Week 10: Multiple local or remote MCP servers
    ↓
Week 12: Deploy and monitor an MCP-enabled agent
```

By the end, the agent will be able to discover server capabilities, invoke MCP tools, read MCP resources, handle unavailable servers, and request approval before consequential operations.

## Week 1: Python fundamentals

### Learn

- Variables, strings, numbers, and booleans
- Conditions and loops
- Functions and parameters
- Lists and dictionaries
- Modules and package installation
- Basic classes and type hints

### Build

Create a command-line task manager that can add, list, complete, and remove tasks.

### Completion checkpoint

You can organize a small Python program into functions and explain the data flowing through it.

## Week 2: APIs, JSON, files, and asynchronous code

### Learn

- Reading and writing files
- Encoding data as JSON
- HTTP requests and responses
- Environment variables and secrets
- Exceptions and error handling
- Virtual environments
- The purpose of `async` and `await`

### Build

Persist the task manager to a JSON file and connect it to a simple external API.

### Completion checkpoint

You can call an API, process its JSON response, and handle common failures.

## Week 3: LLM application fundamentals

### Learn

- System, user, and assistant messages
- Tokens and context windows
- Model selection and temperature
- Instructions versus application logic
- Structured output
- Hallucinations and nondeterministic behavior
- Conversation-history management

### Build

Create a command-line assistant that accepts a request and returns a structured response.

### Completion checkpoint

You can send messages to a model and reliably parse the response into a Python object.

## Week 4: Tool calling

### Learn

- Tools as ordinary application functions
- JSON schemas for tool arguments
- Tool selection by a model
- Argument validation
- Returning observations to the model
- Timeouts, errors, and safe allowlists

### Build

Give the assistant at least these tools:

```python
search_notes(query)
save_note(title, content)
get_current_time()
```

### Completion checkpoint

The model selects an appropriate tool, your application executes it, and the model uses the result correctly.

## Week 5: The agent loop and MCP fundamentals

### Learn

- Goals, actions, and observations
- Repeated model-tool interaction
- Stop conditions
- Maximum-step limits
- Retry and error-recovery strategies
- Human approval checkpoints
- Preventing infinite loops
- The MCP host, client, and server roles
- MCP capabilities: tools, resources, and prompts
- Capability discovery and negotiation
- The difference between direct function calling and MCP
- Inspecting and testing a local MCP server

### Core loop

```text
Receive goal
    ↓
Model chooses an action
    ↓
Application validates it
    ↓
Tool executes
    ↓
Model observes the result
    ↓
Continue or finish
```

### Build

Create an agent that completes a research task through several tool calls. Then build a small local MCP server that exposes `search_notes` and `save_note` as tools.

### Completion checkpoint

The agent can finish a multi-step task without you manually selecting each action, and the local MCP server can be inspected and called independently.

## Week 6: State, retrieval, and MCP integration

### Learn

- State within a single run
- Summarizing long conversations
- Embeddings and semantic similarity
- Document chunking
- Retrieval-augmented generation
- Vector stores and metadata filters
- Connecting an agent to an MCP server as a client
- Discovering tools and resources at runtime
- Mapping MCP results into agent observations
- Handling MCP timeouts, invalid responses, and unavailable servers

### Build

Let the agent index and search a small collection of your own documents. Expose the collection as an MCP resource and connect the research agent to the Week 5 MCP server.

### Completion checkpoint

The agent discovers the MCP server's capabilities, invokes its tools, retrieves relevant passages from its resource, and bases its response on those passages.

## Week 7: Long-term memory

### Learn

- The difference between state, knowledge, and memory
- Deciding what should be remembered
- Memory relevance, confidence, and expiration
- Updating and deleting memories
- Preventing incorrect information from becoming permanent

### Build

Let the agent remember selected user preferences across separate sessions.

### Completion checkpoint

You can explain why every stored item belongs in conversation state, retrieved knowledge, or long-term memory.

## Week 8: Planning and workflows

### Learn

- Breaking goals into tasks
- ReAct-style action and observation
- Plan-and-execute patterns
- Replanning after failure
- Deterministic workflows versus model-driven decisions
- Recognizing when an agent is unnecessary

### Build

Implement this research workflow:

```text
Clarify topic → create plan → gather sources → verify claims → write report
```

Use normal application code for predictable steps and model judgment only where it is valuable.

### Completion checkpoint

The system can detect an insufficient result and revise its plan.

## Week 9: Evaluations and reliability

### Learn

- Test datasets and expected behaviors
- Task-completion scoring
- Tool-selection accuracy
- Model-based graders
- Regression testing
- Tracing and structured logs
- Measuring cost, latency, and token usage
- Prompt-injection and unsafe-action defenses
- MCP capability and tool-selection tests
- Treating MCP tool and resource output as untrusted input
- Simulating server failures, malformed results, and timeouts

### Build

Create at least 20 representative test cases and measure:

- Task completion
- Correct tool selection
- Citation quality
- Invalid arguments
- Number of steps
- Cost and execution time
- MCP discovery and invocation success
- Safe behavior when an MCP server is unavailable or malicious

### Completion checkpoint

You can change a prompt or model and use evidence to determine whether the system improved.

## Week 10: Agent framework, SDK, and production MCP

### Learn

Evaluate a framework based on its support for:

- Tool registration
- State management
- Tracing
- Durable execution
- Human approval
- Evaluations
- Deployment
- MCP client support and server lifecycle management

Also learn:

- Connecting to multiple MCP servers
- Choosing between local and remote transports
- Authentication, secrets, and least-privilege access
- Namespacing or resolving tools with similar names
- Timeouts, retries, reconnection, and partial availability
- Approval gates for consequential MCP tools
- Logging and tracing MCP discovery, calls, and results

### Build

Rebuild your existing agent with one framework or SDK and connect it to at least two MCP servers. One must be your custom learning-progress server; the other can provide notes, files, search, or another bounded capability. Preserve the evaluation suite so you can compare implementations.

The target architecture is:

```text
Research agent (MCP host/client)
├── Notes or documents MCP server
├── Search or reference MCP server
└── Custom learning-progress MCP server
```

### Completion checkpoint

You understand which parts are provided by the framework, MCP, and your application logic. The agent can discover and use multiple servers and degrade safely when one is unavailable.

## Week 11: Multi-agent patterns

### Learn

- Delegation and handoffs
- Supervisor-worker systems
- Shared versus isolated context
- Parallel work
- Conflict resolution
- Added cost and failure modes

### Build

Experiment with three roles:

- Researcher
- Fact-checker
- Report writer

Compare this system with the single-agent version. Retain the multi-agent design only if evaluations justify the complexity.

### Completion checkpoint

You can explain why each role needs to be a separate agent rather than a function, tool, or workflow step.

## Week 12: Production deployment

### Learn

- Web APIs with FastAPI or a similar framework
- Databases and authentication
- Background jobs
- Streaming responses
- Retries and idempotency
- Rate limits and spending budgets
- Secrets management
- Monitoring and audit logs
- User permissions and approval interfaces
- Deploying or connecting to a remote MCP server securely
- Monitoring MCP server availability, latency, and tool failures

### Build

Deploy the research assistant behind an API with a small user interface.

### Completion checkpoint

Another person can use the agent safely without access to your development environment.

## Principles to follow throughout

1. Build one agent incrementally instead of starting a new project every week.
2. Prefer normal code for deterministic operations.
3. Use a model when interpretation or judgment is genuinely needed.
4. Validate every tool call before execution.
5. Require approval for consequential or irreversible actions.
6. Add step, time, and cost limits to every agent loop.
7. Treat model output as untrusted input.
8. Measure behavior with evaluations instead of relying on impressive demonstrations.
9. Add memory only after defining why information should be retained.
10. Introduce multiple agents only when evaluation results justify them.

## Topics to avoid at the beginning

- Large multi-agent architectures
- Heavy frameworks before understanding the agent loop
- Treating prompt engineering as the entire discipline
- Unrestricted file, shell, database, or network access
- Long-term memory without retention rules
- Judging quality from only a few successful examples
- Using an agent where a regular function or fixed workflow is sufficient

## Final success criteria

At the end of the plan, you should be able to:

- Design an agent from first principles
- Implement a controlled model-tool loop
- Build and test a custom MCP server with tools and resources
- Connect an agent to local and remote MCP servers as an MCP client
- Discover capabilities and select tools across multiple MCP servers
- Secure, evaluate, and monitor MCP interactions
- Choose between a workflow, a single agent, and multiple agents
- Manage context, retrieval, and long-term memory separately
- Build safety and approval boundaries
- Evaluate reliability, cost, and latency
- Deploy and monitor an agent for real users
