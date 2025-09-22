# text-summarizer-project

**pyproject.toml setup**

1. **Filename Typo**
   it should be **`setup.cfg`**.
   Otherwise, setuptools won’t recognize your config.

2. **Package Layout**
   Your entry point is:

   ```ini
   [options.entry_points]
   console_scripts =
       mlp = text_summarization.cli:main
   ```

   That means you need this structure:

   ```
   src/
       text_summarization/
           __init__.py
           cli.py
   ```

   Otherwise, `text_summarization.cli` won’t be importable.
   (Right now you showed `cli.py` by itself — make sure it’s inside the package folder.)

---

### 2. Installing Your CLI Locally

From the root of your project (where `setup.cfg` and `pyproject.toml` live), run:

```bash
pip install -e .
```

* `-e` means "editable mode" → if you change your code, you don’t need to reinstall.
* This will install your package and register the CLI entry point `mlp`.

---

### 3. Running Your CLI

After installing, you can test it directly in the terminal:

```bash
mlp
```

Expected output:

```
Welcome to the MLP CLI. Use --greet to receive a personalized greeting.
```

If you run with the argument:

```bash
mlp --greet Francis
```

Expected output:

```
Hello, Francis! Welcome to the MLP CLI.
```

---

Summary:

* Rename `setup.cgf` → `setup.cfg`
* Ensure `cli.py` is inside `src/text_summarization/`
* Install locally with `pip install -e .`
* Run the command as `mlp` (with or without `--greet`).
