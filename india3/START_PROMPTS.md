# INDIA3 START PROMPTS

Every clean role chat must use a hard GitHub preflight. It must open the repository, perform an actual read and an actual write-capability check, and base execution on `pipeline/ENTRYPOINT.md` plus `pipeline/NEXT_ACTION.yaml`, not only on pasted instructions. When either read or write is unavailable, answer exactly `MARK: IK MIS GITHUB CONNECTOR!`.

## CONTROLLER
`GitHub INDIA3 CONTROLLER — open repository bnzgxknwrv-tech/india-knowledge-base. Perform actual GitHub read and write-capability checks. Without both answer exactly MARK: IK MIS GITHUB CONNECTOR! Read pipeline/ENTRYPOINT.md, pipeline/ACTIVE_SYSTEM.yaml and pipeline/NEXT_ACTION.yaml and execute only the indicated controller task.`

## BRONS
`GitHub BRONS — open repository bnzgxknwrv-tech/india-knowledge-base. Perform actual GitHub read and write-capability checks. Without both answer exactly MARK: IK MIS GITHUB CONNECTOR! Read pipeline/ENTRYPOINT.md and pipeline/NEXT_ACTION.yaml, then read only the pinned BRONS context and its required files. Execute only BRONS; do not repair controller state or create successor context.`

## ZILVER
`GitHub ZILVER — open repository bnzgxknwrv-tech/india-knowledge-base. Perform actual GitHub read and write-capability checks. Without both answer exactly MARK: IK MIS GITHUB CONNECTOR! Read pipeline/ENTRYPOINT.md and pipeline/NEXT_ACTION.yaml, then read only the pinned ZILVER context and its required files. Execute only ZILVER; do not repair controller state or create successor context.`

## GOUD
`GitHub GOUD — open repository bnzgxknwrv-tech/india-knowledge-base. Perform actual GitHub read and write-capability checks. Without both answer exactly MARK: IK MIS GITHUB CONNECTOR! Read pipeline/ENTRYPOINT.md and pipeline/NEXT_ACTION.yaml, then read only the pinned GOUD context and its required files. Execute only GOUD; do not repair controller state or create successor context.`

## RESUME AFTER FAILURE
`GitHub INDIA3 CONTROLLER — open repository bnzgxknwrv-tech/india-knowledge-base. Perform actual GitHub read and write-capability checks. Without both answer exactly MARK: IK MIS GITHUB CONNECTOR! Read pipeline/ENTRYPOINT.md, pipeline/NEXT_ACTION.yaml and the active failure/status file. Resume only the first incomplete validated controller step.`

## NEW FULL RESEARCH RUN
`GitHub INDIA3 CONTROLLER — perform the hard GitHub preflight, then create the next full research run from pipeline/ENTRYPOINT.md.`

## CORRECTION RUN
`GitHub INDIA3 CONTROLLER — perform the hard GitHub preflight, then create or resume the bounded correction run named by Mark and follow pipeline/ENTRYPOINT.md.`

## GEO RECOVERY RUN
`GitHub INDIA3 CONTROLLER — perform the hard GitHub preflight, then create or resume the bounded GEO recovery run and follow pipeline/ENTRYPOINT.md.`

## REGENERATE MARK DELIVERY ONLY
`GitHub GOUD — perform the hard GitHub preflight and execute only the pinned delivery-regeneration action from pipeline/ENTRYPOINT.md and pipeline/NEXT_ACTION.yaml.`

END_OF_ARTIFACT