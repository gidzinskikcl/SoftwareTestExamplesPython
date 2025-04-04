# SoftwareTestExamplesPython

This simple project was created to demonstrate my approach to software testing in Python (in progress).

## Software Description:

The Calendar Application is an online platform designed to help users organize their schedule. It allows users to create events, view schedules, set reminders, and apply filters based on event categories or dates. The system supports recurring events, time zone handling, and different views (e.g., daily, weekly, monthly). Additionally, the system provides reminders for upcoming events and allows users to sync their events with external calendar systems.

## System Requirements:

**1. User Account Management**

- Users shall be able to create an account, log in, and manage their profile (e.g., change email, password).

**2. Event Creation**

- Users shall be able to create events with the following attributes:
  - **Event Name**
  - **Description**
  - **Date and Time**
  - **Duration**
  - **Event Category** (e.g., Work, Personal, Meeting, etc.)
  - **Recurrence** (e.g., Daily, Weekly, Monthly)
  - **Location** (Optional)

**3. Event Viewing and Filtering**

- Users shall be able to view events in multiple formats:
  - **Daily View, Weekly View, Monthly View**
- Users can filter events by:
  - **Category** (e.g., Work, Personal)
  - **Date Range** (e.g., Today, Next 7 days)

**4. Event Reminders**

- The system shall allow users to set reminders for events:
  - **Reminder Time** (e.g., 30 minutes before, 1 hour before, etc.)
  - Multiple reminders per event
  - Notifications via email or push notification

**5. Recurring Events**

- Users shall be able to create recurring events with different recurrence patterns:
  - **Daily, Weekly, Monthly**
- The system shall correctly handle multiple instances of recurring events.

**6. Event Modification and Deletion**

- Users shall be able to modify or delete events, including modifying recurrence rules or individual event instances.

**7. Time Zone Handling**

- The system shall handle events in different time zones and display the event time adjusted to the user's local time zone.

**8. Event Sharing**

- Users shall be able to share event details with others via email or a public link.

**9. Search Functionality**

- Users shall be able to search for events **Name, Description, Category**

**10. Event Conflict Detection**

- The system shall prevent users from creating events that conflict with existing events (e.g., two events scheduled for the same time).

**11. Authentication and Authorization**

- The system shall authenticate users using secure methods (e.g., email/password).
- Unauthorized users should not be able to create, modify, or delete events.

**12. Privacy Settings**

- Users shall be able to set privacy settings for their events:
  - **Public, Private, Shared**

**13. Calendar View Navigation**

- The system shall allow users to navigate between different months, weeks, and days using navigation buttons or calendar date selection.

**14. Event Export**

- Users shall be able to export their calendar events to a file format such as `.ics` (iCalendar) for use with other calendar applications.
