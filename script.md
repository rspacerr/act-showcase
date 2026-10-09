# Act CLI

Showcase project and CI

Run unittests as proof of concept
```sh
uv run python -m unittest tests.test_utils
```

Build dist
```sh
uv build
```

## Now, let's run our workflows with act!


```sh
act
```

Uh oh!
```sh
act -P ubuntu-latest=catthehacker/ubuntu:act-latest -j tests
```

Fix errors
Run `vermin`
Create PR

