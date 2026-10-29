from pathlib import Path
import csv, json, zipfile

p=Path(__file__).resolve().parent
d=json.loads((p/'data/pilot_matrix.json').read_text(encoding='utf-8'))
ids=[r['record_id'] for r in d['register']]
assert len(ids)==len(set(ids))
for group in ['primary_matrix','prior_reviews','review_dimensions','optimization']:
    assert all(r['record_id'] in ids for r in d[group]), group
assert len(d['primary_matrix'])==26
assert len(d['prior_reviews'])==8
assert len(d['optimization'])==7
assert sum(bool(r['doi']) for r in d['register'])==118
assert all(r['verifier_status']=='awaiting_independent_verification' for r in d['primary_matrix'])
with (p/'data/review_study_edges.csv').open(encoding='utf-8-sig',newline='') as f:
    assert not list(csv.DictReader(f)), 'Overlap edges have changed: review completeness before calculating overlaps'
if (p/'initial_review_matrix.xlsx').exists():
    with zipfile.ZipFile(p/'initial_review_matrix.xlsx') as z:
        assert len([n for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')])==7
print(json.dumps(dict(records=len(ids),primary_rows=26,review_rows=8,optimization_rows=7,overlap='Not computed; no extracted inclusion edges')))
