# GITHUB WRITE PROTOCOL

Before writing, fetch current HEAD and required file SHAs. Use atomic tree/commit writes for multi-file phase completion. Never update the same path concurrently.

Allowed write scopes are role-specific. A SHA conflict triggers one fresh read and safe rebase/reconstruction attempt. If conflict remains or input meaning changed, stop and write failure status without overwriting valid work.

After every commit, read back critical files, verify content sentinels/status and confirm branch ref equals the intended commit. Phase completion and claim closure occur in the same commit.

END_OF_ARTIFACT
