# AGENTS.md

This file defines how agents should work in this repository.

These instructions apply repo-wide unless the user gives a more specific request.

## Intent

This role should stay simple, explicit, and production-friendly.

The goal is not to support every possible Compose workflow. The goal is to provide
a small, coherent API that is easy to read, easy to review, and safe to run on an
already running host.

## Expected style

- Prefer clarity over cleverness.
- Prefer one clean public API over several overlapping inputs.
- Prefer removing dead code and dead variables over keeping backwards-compatible noise.
- Prefer explicit names that describe intent, not implementation detail.
- Keep tasks small and easy to scan.
- Do not leave debug tasks or temporary troubleshooting code in the final role.

## What good Ansible looks like here

- Use FQCNs for modules.
- Use explicit task names that describe the action.
- Use Ansible modules instead of `shell` or `command` whenever a proper module exists.
- Use YAML booleans as `true` and `false`, never `yes` or `no`.
- Fail fast on invalid states instead of silently working around them.
- Keep role inputs typed and structured as lists of dictionaries when the feature is repeatable.
- Keep defaults minimal and truthful: if a variable is exposed in `defaults/main.yml`, it must be supported end-to-end by the role.
- Avoid feature flags for half-supported behavior.

## Public API rules

- Public variable names must reflect the real contract of the role.
- Prefer intent-driven names like `compose_deploy_projects` over overly generic names like `folders`.
- Do not keep several competing ways to describe the same thing unless there is a strong reason.
- If the role deploys project directories, standardize on project directories.

Current preferred API:

```yaml
compose_deploy_projects:
  - name: myapp
    src: files/myapp/
    dest: /opt/myapp
    mode: "0644"
    directory_mode: "0755"

compose_deploy_volumes_dir:
  - path: /srv/myapp/data
    mode: "0755"
```

## Idempotence and safety

This repository values safe behavior on hosts that may already be running containers.

- Never change permissions on an existing Docker-managed volume directory unless the user explicitly asks for it.
- For bind-mount directories, check the current state before creating anything.
- If a directory does not exist, create it with the requested mode.
- If the path exists and is not a directory, fail clearly.
- If the directory already exists with a different mode, do not "fix" it automatically; skip the permission change and explain why.
- Avoid `recurse: true` on existing application or volume paths unless the user explicitly wants recursive permission normalization.
- Avoid destructive behavior hidden behind "idempotence".

## Compose-specific expectations

- A Compose project should be treated as a self-contained directory that can be copied and deployed as-is.
- The role should deploy from `project_src`, not rebuild application structure from many fragmented variables.
- Keep the remote layout predictable.
- Prefer a complete project tree over a mix of manifest files, template files, and ad hoc config file copies.

## Task design

- Group tasks by purpose: prerequisites, validation, filesystem prep, project sync, deploy.
- Use `loop_control.label` when looping over paths or project items.
- Register intermediate facts only when they are used by following tasks.
- Keep `when` conditions explicit and readable.
- Avoid deep Jinja expressions inline when a clearer approach exists.

## Testing and validation

Before considering a change done, run what is available locally:

- `yamllint`
- `ansible-lint`
- `molecule` when Docker access is available

For scenario verification, use Ansible `verify.yml` playbooks.
Tests in this repository are now written in Ansible, not in Python.
Do not introduce new `testinfra` or Python-based verification tests.

If a full runtime test cannot be executed because of sandbox or Docker access limitations,
say so clearly in the final report.

## Documentation expectations

- Code can move before docs while the API is being refactored.
- Once the API is stabilized, README examples must match the real role contract.
- Do not leave documentation for removed variables or removed workflows.
- Examples should be runnable, not aspirational.

## When to ask the user

Ask before implementing if the answer changes the public contract of the role, for example:

- supported project structure
- overwrite policy for existing files
- ownership handling
- backward compatibility vs cleanup

If the intent is already clear, implement directly.
