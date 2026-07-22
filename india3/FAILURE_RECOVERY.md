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

## Controller-transition defects
Placeholders, absent or stale blob SHAs, wrong manifest paths, circular activation dependencies and PREPARING status are controller-owned defects. BRONS, ZILVER and GOUD stop before substantive work and do not bypass or repair them. The controller repairs them autonomously when canonical intent is unambiguous.

A repaired transition uses PREPARING, exhaustive manifest readback and a final NEXT_ACTION activation write. The controller records the defect and durable protocol lesson so the same failure class receives a structural test rather than only a one-run patch.

A new chat verifies current repository state, reads only the status-listed required files and resumes at the first incomplete validated step. It never restarts completed role work.

GitHub read/write failure is reported only as `MARK: IK MIS GITHUB CONNECTOR!` because no reliable status commit can be guaranteed.

END_OF_ARTIFACT