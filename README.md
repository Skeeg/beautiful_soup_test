# beautiful_soup_test

Quick project that uses python and the beautiful soup library to query the Exvius wiki for NV Unit Awakenings that are still pending.

## Usage

Using pipenv to create a python virtual environment, you can use this to parse the release table, currently filtered to the Season 4 header.

After entering the project directory after cloning, then you can run the following commands.

```bash
pipenv install
pipenv shell
python3 ./ffbe_nv_unit_awakening.py
```

Switch it up a little by getting some colors in your output with jq, ala: `python3 ./ffbe_nv_unit_awakening.py | jq -c .`
