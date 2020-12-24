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
tags() {
  cd src
  ctags -R .
  cd ..
}
r() { run; }
t() { test; }
c() { testcover; }
tc() { testcover; }
