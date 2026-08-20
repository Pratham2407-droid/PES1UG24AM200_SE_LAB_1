# Academic Elective Bidding & Allocation System

## Problem Statement

**Problem Statement 05 - Campus & Academic Operations**

The Academic Elective Bidding & Allocation System is designed to manage the process of elective course selection through a bidding-based allocation system.

Students can view available electives, check eligibility, distribute their bidding credits, and submit their preferences. The system validates submitted bids and helps allocate electives while considering constraints such as prerequisites and timetable conflicts.

### Target Actors

- Student
- Academic Registrar

---

## Deliverables

### Deliverable 1: Requirements Table

The requirements table contains:

- 5 Functional Requirements (FR-001 to FR-005)
- 2 Non-Functional Requirements (NFR-001 to NFR-002)

Each requirement contains the following fields:

1. Requirement ID
2. Type
3. Description
4. Priority
5. Acceptance Criteria
6. Rationale

The requirements are stored in both JSON and HTML formats inside the `requirements` folder.

---

### Deliverable 2: UML Use-Case Diagram

The UML use-case diagram represents the interaction between the system and its actors.

#### Actors

- Student
- Academic Registrar

#### Student Use Cases

- Login
- View Available Electives
- Check Prerequisites
- Allocate Bidding Credits
- Submit Bids
- View Allocation Result
- Validate Bids
- Check Credit Limit
- Modify Bids

#### Academic Registrar Use Cases

- Login
- Manage Elective Courses
- Configure Bidding
- Run Elective Allocation
- Resolve Allocation Conflicts
- Publish Allocation Results
- Check Timetable Conflicts

The UML diagram contains:

- Actor associations
- `<<include>>` relationships
- `<<extend>>` relationship
- System boundary

The editable Draw.io source is stored in the `uml` folder.

---

### Deliverable 3: Use-Case Flow Specification

The main use case documented is:

**UC-01: Submit Elective Bids**

The specification contains:

- Use-case description
- Primary actor
- Secondary actors
- Trigger
- Preconditions
- Postconditions
- Main Success Scenario
- Alternate Flow A1
- Alternate Flow A2

---

## Main Use Case

### UC-01: Submit Elective Bids

The student selects and ranks elective preferences, distributes bidding credits, and submits the bid.

The system checks the bidding credit limit and verifies prerequisite requirements before accepting the bid.

### Main Flow

1. Student selects and ranks elective preferences.
2. System displays available bidding credit balance.
3. Student distributes bidding credits.
4. System validates the total credit allocation.
5. System checks prerequisite requirements.
6. Student confirms and submits the bid.
7. System stores the valid bid.
8. System displays a submission confirmation.

---

## UML Relationships

### Include Relationships

- Submit Bids `<<include>>` Validate Bids
- Allocate Bidding Credits `<<include>>` Check Credit Limit
- Run Elective Allocation `<<include>>` Check Timetable Conflicts

### Extend Relationship

- Modify Bids `<<extend>>` Submit Bids

---

