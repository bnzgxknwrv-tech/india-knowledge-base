# FAILURE RECOVERY

Before stopping, write a machine-readable failure report and update run or migration status with:
- failure code and scope;
- last valid commit;
- active role and state;
- completed checks;
- failed check and one attempted repair;
- files that remain valid;
- files that must not be overwritten;
- next exact action;
- exact clean-chat resume prompt.

A new chat verifies HEAD and the last valid commit, reads only the status-listed required files and resumes at the first incomplete validated step. It never restarts a completed iteration or phase.

GitHub read/write failure is reported only as `MARK: IK MIS GITHUB CONNECTOR!` because no reliable status commit can be guaranteed.

END_OF_ARTIFACT
