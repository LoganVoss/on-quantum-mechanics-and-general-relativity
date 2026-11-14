from pathlib import Path
import sympy as s, json, hashlib
q,A=s.symbols('q A',positive=True)
h=q**5;eta=q**2;N=A*A*q**-26
checks={
 'population_diagonal_rms':s.simplify(A/(s.sqrt(N)*h)-q**8),
 'mollifier_bias':s.simplify(eta**2-q**4),
 'midpoint_current_term':s.simplify(h*h*eta**-3-q**4),
 'quantum_position_current_term':s.simplify(q**8*eta**-2-q**4),
 'rounding_path_current_term':s.simplify(1/(N*h*h)*eta**-2-q**12/A**2),
 'rounding_weight_current_term':s.simplify(1/(N*h*h)*eta**-1-q**14/A**2),
 'classical_path_current_term':s.simplify(h*h*eta**-2-q**6),
 'classical_amplitude_current_term':s.simplify(h*h*eta**-1-q**8),
}
for k,v in checks.items():assert v==0,(k,v)
# Derivative/source version of the root functional-calculus integral.
t,m=s.symbols('t m',positive=True)
assert s.integrate(s.sqrt(t)/(m*m+t)**2,(t,0,s.oo))/s.pi==1/(2*m)
assert s.integrate(s.sqrt(t)/(m*m+t)**3,(t,0,s.oo))/s.pi==1/(8*m**3)
report={'status':'PASS','exact_check_count':10,'scaling_residuals':{k:str(v)for k,v in checks.items()},'scope':'Checks the integrated parameter exponents and functional-calculus constants. Analytic stage hypotheses and full proofs are separate.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('synthesis_receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
