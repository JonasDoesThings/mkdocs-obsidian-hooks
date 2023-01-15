# mkdocs obsidian hooks
A collection of useful mkdocs hooks that improve compatibility between Obsidian.md and mkdocs.

---

## Installation
Add the following to your `mkdocs.yml` configuration:

```yaml
hooks:
  - PATH_TO_YOUR_HOOK/HOOK_NAME.py
```

The path is relative to the `mkdocs.yml` config file location. For more information see the official mkdocs docs: https://www.mkdocs.org/user-guide/configuration/#hooks

---

## Hooks

### strip_obsidian_comments.py
**Description:** This hook strips out comments in the ObsidianMD comment format (%% <comment> %%)

**Examples:**
```markdown
%% this inline comment will be removed from your mkdocs output %%

%% multi
line comments
also get __removed__%%

%%this
*gets removed*
%%

**this here will stay in, since it's no comment**
```