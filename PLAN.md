# Transport network disruption and resilience: review-paper plan

Version 0.1 | 29 October 2026 | Proposed protocol and pilot, not a completed systematic review

## Proposed article

Working title: **From disruption models to defensible decisions: a critical evidence map of transport network resilience research**.

The paper should explain what different modeling choices allow researchers and decision makers to conclude. Its contribution would be a decision-oriented synthesis supported by a systematic evidence map, an explicit comparison of preceding reviews, and an auditable coding dataset. Maps and bibliometric networks should support that argument rather than replace it.

The recommended design is a systematic scoping review with critical methodological synthesis and a linked review-of-reviews component. This is a proposed design choice, not a claim that the existing convenience corpus is systematic or representative. No meta-analysis of heterogeneous resilience scores or monetary losses is planned. An umbrella review alone would be insufficient because we also need to inspect primary models.

Transport Reviews asks for authoritative, critical, current and accessible synthesis that adds value and reaches conclusions grounded in the reviewed literature. Its scope does not support turning this paper into a new transport simulation study. Bibliographic and coding analyses are secondary analyses of the reviewed evidence; any new experimental benchmarking should be a separate project. Exact word limits and current submission requirements must be rechecked before submission; the author-instruction page was inaccessible during planning. [S1-S2]

## Research questions

1. What have earlier reviews covered, how did they organize the field, and where do their questions, study sets and conclusions overlap or differ?
2. How do primary studies connect hazard representation, networks and flows, time and recovery, and consequence measures? Which combinations are represented and how well are they supported?
3. What decisions do optimization studies address, what do they optimize, and how do their assumptions, constraints and validation affect the usefulness of their recommendations?
4. Where and by whom is the research produced, where are the case studies located, and which contexts and transport systems are poorly represented in the eligible corpus?
5. What minimum reporting, model-selection guidance and research designs would make future findings more comparable and useful?

## Scope and eligibility to freeze before searching

Use two connected evidence layers. Layer R includes relevant transport resilience/vulnerability/disruption reviews, bibliometric syntheses and close cross-sector methodological reviews. Layer P includes primary studies of transport-network functionality, mobility/flow disruption, or prescriptive resilience decisions under natural or anthropogenic disruption. Separate empirical observation, topology/accessibility, demand-loaded routing/assignment, hazard-to-damage modeling, economic coupling, and optimization rather than imposing an assigned-flow eligibility test on every study. That broader scope is deliberate for a review paper and differs from the narrower comparison supporting the existing US application.

Road networks are the anchor; rail-road and other surface/multimodal systems are eligible when they inform interaction, substitution, propagation, freight or passenger decisions. Aviation/maritime-only and interdependent-infrastructure work may be contextual unless transport-network consequences or transferable decisions are central. Asset-only work belongs in a contextual boundary layer, not in a denominator labeled flow-model studies. Relief logistics and evacuation are explicit subgroups; do not silently merge them with ordinary freight and commuting demand. Include stylized optimization networks but code realism and transferability rather than excluding them for lacking a real case.

Current-primary stratum: 1 January 2019 through the final search date, with an update before submission. Earlier reviews have no 2019 cutoff. Pre-2019 primary studies form a separately labeled historical bridge, selected through documented conceptual/methodological links and citation tracing. Analyze the 2019+ stratum separately for frequency and time trends; selected older examples are not a representative historical corpus. This implements the preference for recent work without erasing foundational methods. A full historical census is an alternative scope expansion, requiring a protocol amendment.

English full texts are the proposed working language, not a claim of language-complete coverage. Record language exclusions and their likely geographic effects. Journal articles and substantive peer-reviewed conference studies are eligible; reports/preprints can inform context or historical origins, with publication status retained and study families linked. Lack of immediate PDF access is not a scientific exclusion: log retrieval attempts and reports not retrieved separately. Exclude editorials without substantive synthesis, unrelated traffic-control studies without disruption, and component-material studies without network implications from primary analytical synthesis.

## Reporting and conduct

Use JBI scoping-review methodology to structure conduct, PRISMA-ScR for the reporting checklist, PRISMA-S for reproducible searching, and the appropriate PRISMA flow diagram for records/reports/studies. PRISMA is reporting guidance, not a conduct protocol, a risk-of-bias instrument, or certification. PRISMA 2020 can inform record accounting and relevant reporting items without claiming that a scoping review is an intervention-effect review. Seek information-specialist review of the principal search strategy using PRESS principles. Use evidence-map guidance when choosing and documenting the framework and display. [S3-S7]

Freeze a dated protocol before formal searching and archive amendments. A public or private timestamped protocol repository/OSF registration is suitable if available; do not imply that registration or dual screening has already happened. Distinguish human decisions, AI-assisted extraction and independent verification. Save tool/model versions, extraction prompts, dates, source versions and corrections. Two AI readings do not constitute two independent human reviewers.

## Search and screening workflow

1. Reconcile the current bibliography into report and study-family identifiers. The existing Undermind searches and Zotero PDFs are seeds, not the complete search universe. Do not reuse their counts as PRISMA identification totals.
2. Develop searches for both reviews and primary studies in Scopus, Web of Science and TRID; supplement with suitable engineering indexing, backward/forward citation tracing, and Undermind discovery. Confirm licensed database access through GMU. Search across venues; Transportation Research Parts A-F are an important subset, not an eligibility restriction for Transport Reviews.
3. Use concept blocks for transport/network; disruption/resilience/vulnerability; and hazards/operations. Run supplementary optimization/recovery decision searches because many decision papers do not use resilience terminology. Test recall against diverse sentinel studies and reviews. Translate proximity/field syntax for each platform rather than claiming a universal executable query.
4. Log every executed database/platform, exact query, fields/limits, date/time, returned count, exported count and export filename/hash. Save full exports before deduplication. Log citation tracing and Undermind as separate discovery routes.
5. Deduplicate DOI-normalized reports, then resolve title/author/year matches and preprint/report/journal families manually. A shared network or event does not automatically make two papers duplicates; record genuinely distinct contributions within a study family.
6. Pilot eligibility on a mixed sample and revise the codebook. Two human reviewers should screen independently, reconcile disagreements and record adjudication. If only one reviewer is feasible, declare the departure and arrange an independent sample check; do not label it dual screening.
7. Keep title/abstract and full-text decisions separate. At full text use one primary exclusion reason from a frozen hierarchy and optional secondary notes. Distinguish duplicate reports, wrong scope, non-substantive methods, and unavailable reports. Reconcile the flow diagram from the event log; never fill it with guessed counts.

Pilot calibration target: 15-20 diverse studies and 3 reviews, deliberately spanning observation, accessibility, assignment, hazard damage, restoration and optimization. This is a proposed work package, not a sample-size requirement imposed by PRISMA. Compare agreement per field, not only a single overall score; investigate disagreements before scaling up. No automated inclusion/exclusion decisions without human confirmation.

## Coding architecture

Use linked tables rather than one unmanageable sheet. Bibliographic records identify reports; study families link versions; review records describe syntheses; primary-study rows capture applications; optimization rows capture distinct decision problems; cases/affiliations support geography; review-study edges support overlap; and evidence rows support individual codes.

The four themes remain the core. Add cross-cutting provenance, study purpose, evidence/validation, uncertainty, reproducibility, equity, environmental impacts and optimization. The codebook separates proposed capability from demonstrated application and permits multiple codes. Keep Yes/No/Partial only as a presentation view derived from explicit rules; raw extraction must retain the method and its limitation. Use **unassessed**, **not_reported**, **not_applicable**, and **reported_absent** as distinct states. An empty cell is not No.

For every consequential code, retain report ID, field, extracted value, source version, page/section/table, evidence basis, extractor, verifier and adjudication state. The pilot is AI-assisted/single-pass and awaits independent verification. Inherited v3 summaries have page/section provenance but do not imply that every new codebook field was extracted.

## Explicit treatment of preceding reviews

For each review record the question and angle, scope, search date and coverage, databases, inclusion/exclusion rules, review type, number and unit of included records, selection transparency, taxonomy dimensions, treatment of optimization/validation/uncertainty, conclusions, stated limitations, and the availability of a true inclusion roster.

The pilot already shows meaningful distinctions. Faturechi and Miller-Hooks cover concepts, life-cycle phases, measures, uncertainty and optimization. Rebally et al. organize flood assessment by impact type and spatial/temporal scales. Hassan et al. combine bibliometrics with six assessment families. Verschuur et al. compare infrastructure sectors and systemic-risk tiers. Nirandjan et al. focus on physical vulnerability curves. Lamei et al. directly examine multimodal freight methods, cascades/recovery and validation. The latter is a particularly close recent comparator, not a review to dismiss as lacking guidance. Mattsson/Jenelius and Sun et al. remain pilot records awaiting fresh full-text extraction. [R1-R8]

Translate each review's own taxonomy into our shared dimensions while retaining its original labels. Distinguish a systematically coded dimension from a topic merely discussed, a stated exclusion, and an unassessed field. A narrow scope is not necessarily a methodological weakness. Audit review transparency with domain-appropriate items; do not apply clinical intervention quality tools or a fabricated numerical quality ranking uncritically.

## Review-overlap analysis

Three distinct questions require three different networks:

- **Evidence overlap:** edges connect reviews that include the same eligible primary studies. Start from explicit inclusion rosters or documented study tables/supplements, not the entire reference list. Store included_core, included_background, cited_only, uncertain and excluded edge types separately. Link reports to study families, so a preprint and journal article do not artificially reduce overlap.
- **Taxonomy overlap:** compare reviews' explicitly coded analytical dimensions. Show their original categories and crosswalk. Topic similarity does not demonstrate shared included evidence.
- **Bibliographic coupling:** common bibliography references measure intellectual context. They may be visualized separately but must never be labeled included-study overlap.

Compute pairwise Jaccard as shared/(A union B), directed containment as shared/size(A) and shared/size(B), and absolute shared counts. For eligible reviews with complete inclusion rosters, also report overall and pairwise corrected covered area (CCA): (N-r)/(r*c-r), where N is study occurrences, r unique studies and c reviews. With fewer than two eligible reviews or r=0 the result is undefined. For two complete reviews, pairwise CCA equals the Jaccard overlap of their included-study sets; do not present them as independent findings. Overall CCA can hide pairwise structure. Do not transfer medical threshold labels mechanically to transport. [S8-S9]

Show the raw, scope-stratified and common-publication-window results. A recent narrow review may be almost contained within an older broad review while having modest Jaccard. Recent unique papers can reflect a later search date rather than a new intellectual angle. If inclusion rosters are unavailable, report missingness and roster completeness; do not replace missing edges with zeros or claim a complete overlap map. Pilot overlap estimates are deliberately not computed yet.

## Optimization as a contribution, not just an algorithm label

Separate descriptive assessment/prediction from prescriptive choice. An equilibrium assignment or shortest-path calculation may be mathematically solved through optimization without being a resilience intervention. A system-optimal assignment is a central-control traffic allocation and needs a behavioral/compliance interpretation. Restoration prioritization by a rule is different from solving a formal scheduling problem.

For each prescriptive problem code: decision maker and user; decision timing (mitigation/preparedness/response/recovery/adaptation); decision variables (hardening, capacity, routing, facilities, service design, crews, repair sequencing, inventories or information); objective(s), units and distributional weights; constraints; uncertainty/information timing; traffic/hazard coupling; mathematical structure; solution method; problem size and runtime; optimality gap/bounds where meaningful; baseline and sensitivity; validation; and implementation requirements. Multiple decision problems in one paper receive separate rows.

Compare the **decision problem**, **model formulation** and **solution algorithm** independently. MILP, stochastic, robust, bilevel, multiobjective, simulation-optimization and reinforcement learning are not mutually exclusive categories. A heuristic's good objective value is not proof of real-world resilience; solver optimality is conditional on the model. Ask what improved, relative to which feasible baseline, at what budget, under which hazards, and whether rankings survive uncertainty or out-of-sample events. Evidence of deployment differs from empirical validation, which differs from a realistic network case.

The pilot optimization sheet uses checked examples: static capacity-restoration choice (Zhao/Zhang), crew allocation (Sun/Zhang), repair sequencing for transport-healthcare access (Pei et al.), evacuation routing with non-compliance (Yu et al.), and greedy reopening (Shen et al.). The final synthesis should connect these choices to the four-theme chain and distinguish user costs from objective proxies.

## Visual analysis and article structure

The figure storyboard is in FIGURES.md. Main figures should answer substantive questions: prior-review coverage/overlap; the geography of authorship versus case evidence; topic/method structure; combinations of the four themes; and decision-method-evidence pathways. Bibliometric counts are not evidence of model validity or research quality. Topic clustering is exploratory and must be checked against full-text coding.

Suggested article structure: Introduction and questions; explicit position relative to prior reviews; methods and evidence selection; research origins and topic structure; critical synthesis across the four themes; optimization and decision support; researcher guidance and research agenda; limitations and conclusions. At drafting, combine sections where this improves readability and check journal length requirements rather than treating this as a fixed word allocation.

## Research guidance and gap claims

Build a model-selection guide starting from the intended decision and outcome: asset repair; connectivity/access; congestion and unmet demand; commodity/passenger incidence; repair-resource decisions; or wider economic propagation. For each identify minimum inputs, justified simplifications, validation evidence, outputs, and conclusions that would exceed the model's scope.

Classify gaps as evidence coverage, missing/weak mechanism, validation, reproducibility, transferability, decision implementation, or inconsistent terminology/valuation. A low cell count is a candidate gap within the searched corpus, not proof that no study exists or that the missing combination is worthwhile. Require a final targeted gap search and check earlier reviews' recommendations before wording a novelty claim. Distinguish an absence of reporting from an absence of implementation.

Positioning to test: **This review links the questions asked of transport resilience models to their hazard, flow, temporal and consequence assumptions, and examines how those assumptions support or limit prescriptive decisions. By comparing earlier reviews and their evidence coverage explicitly, it distinguishes established recommendations from unresolved, decision-relevant research needs.** Do not claim priority until the review-of-reviews and supplementary searches are complete.

## Work packages and completion gates

WP1: scope/protocol/search design; owner lead researcher with information specialist; gate: agreed eligibility, search strategy and codebook v1. WP2: systematic identification/screening; owner two reviewers; gate: reconciled logs and retrieval/exclusion records. WP3: full-text extraction and calibration; owner coders plus verifier; gate: evidence-backed records and resolved critical fields. WP4: prior-review rosters/taxonomy and overlap; gate: completeness reported and only eligible edges analyzed. WP5: primary synthesis, optimization and visuals; gate: sensitivity checks and interpretation validated. WP6: guidance, manuscript and release; gate: source-backed claims, current search, journal check and reproducible tables/figures.

Effort should be estimated after formal retrieval volume and the coding pilot, rather than promising a completion date from the current selected corpus. The immediate next milestone is to approve scope and calibrate the codebook, then run the reproducible searches. This turn prepares the plan and pilot; it does not execute the full review.

## GitHub package and publication boundary

Keep the protocol, codebook, metadata, extraction matrices, search/screening logs, analysis scripts and figure specifications under version control. Keep a changelog and data dictionary. Do not publish subscription PDFs, Zotero database/storage, local source paths, credentials or unpublished draft text through an automatic repository upload. Use links and metadata instead. The proposed upload concerns this plan and initial matrix only.

Destination: https://github.com/AliMurtaza53/TReview_Resilience. Publish this plan and pilot on a dedicated branch with a draft pull request. Source PDFs, Zotero storage and unpublished manuscript files remain excluded. Repository readability and metadata-level push permissions do not guarantee connector write capability; use authenticated repository access and verify the resulting commit and PR.

## Sources

S1. [Transport Reviews aims and scope](https://www.tandfonline.com/journals/ttrv20). S2. [What is a good transport review paper?](https://doi.org/10.1080/01441647.2021.2001996). S3. [JBI definition and methodology](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355862573/10.1.2+What+are+scoping+reviews). S4. [PRISMA-ScR](https://www.prisma-statement.org/scoping). S5. [PRISMA-S](https://www.prisma-statement.org/prisma-search). S6. [PRESS guidance](https://doi.org/10.1016/j.jclinepi.2016.01.021). S7. [Campbell evidence-and-gap-map guidance](https://doi.org/10.1002/cl2.1125). S8. [Pieper et al., overlap and CCA](https://doi.org/10.1016/j.jclinepi.2013.11.007). S9. [Pairwise CCA considerations](https://doi.org/10.1002/jrsm.1658). Publisher pages for the editorial and author instructions returned access errors; no unverified word-limit requirement is asserted.

R1-R8 are the eight DOI-identified records in data/review_pilot.json and data/prior_reviews.csv; detailed pilot evidence is in evidence/prior_review_fulltext_notes.md. These are initial comparators, not an exhaustive review-of-reviews sample.
