## learning
### OieInduction
 - `OieInduction.ReconstructInducer.goldStandard`: `Dict[int, List[str]]`, 
key is the example id, value is relation label name, maybe contains only one value 

## evaluation
### evaluation.OieEvaluation
 - `OieEvaluation.assessableElems`: `Set[int]`, set of rel-example id, whose relation label exists, i.e. "true" cluster

 - `OieEvaluation.referenceSets`: `Dict[str, List[int]]`, key is first word of relation label, 
value is list of example ids   


