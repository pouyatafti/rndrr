#!/bin/sh

TEMPDIR=$(mktemp -d)
for f in tests/*.out; do
    t=${f%.*} 
    tt=${TEMPDIR}/${t#tests/}
    python3 rndrr.py -c $t.toml -f $t.j2 >$tt.out
    diff $t.out $tt.out >/dev/null && echo [$t] ok || echo [$t] failed!
done
rm -rf $TEMPDIR
