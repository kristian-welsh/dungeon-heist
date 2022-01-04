run() { python3 -m src; }
test() {
  coverage run -m unittest discover ./src/test
}
testcover() {
  test
  coverage report
  coverage html
  # brave is a function that opens a webpage
  brave htmlcov/index.html
}
tags() { ctags -R .; }
r() { run; }
t() { test; }
v() { vim src/main/*.py; }
vt() { vim src/test/*.py; }
va() { vim src/main/*.py src/test/*.py; }
c() { testcover; }
tc() { testcover; }
