# Extraction codebook v0.1

Status: proposed field definitions for calibration, not completed coding. Missingness states are unassessed, not_reported, not_applicable and reported_absent. Multi-label fields are retained as text until normalized child tables are extracted.

## record_identity

- **record_id**: Stable report identifier. Rule: One record per report; link versions without automatically merging distinct contributions.
- **study_family_id**: Underlying study/version family. Rule: One record per report; link versions without automatically merging distinct contributions.
- **doi**: Normalized DOI. Rule: One record per report; link versions without automatically merging distinct contributions.
- **year**: Issue publication year; online-first separately retained. Rule: One record per report; link versions without automatically merging distinct contributions.
- **report_type**: Primary, review, contextual, report or preprint. Rule: One record per report; link versions without automatically merging distinct contributions.
- **discovery_sources**: All discovery routes; not a PRISMA count. Rule: One record per report; link versions without automatically merging distinct contributions.

## provenance

- **source_version**: Exact PDF/report version. Rule: Attach to each consequential code; no inferred absence from an abstract.
- **evidence_locator**: Page, section, figure, table or supplement. Rule: Attach to each consequential code; no inferred absence from an abstract.
- **evidence_basis**: Full text, abstract or metadata. Rule: Attach to each consequential code; no inferred absence from an abstract.
- **extractor**: Named human or disclosed AI tool/version. Rule: Attach to each consequential code; no inferred absence from an abstract.
- **verifier_status**: Independent check and adjudication state. Rule: Attach to each consequential code; no inferred absence from an abstract.
- **capability_status**: Demonstrated application versus proposed capability. Rule: Attach to each consequential code; no inferred absence from an abstract.

## review_comparison

- **review_type**: Author-described and assessed review design. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **angle**: Research question and perspective. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **publication_coverage**: Search window and publication years. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **search_method**: Database/platform, strings, limits and execution date. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **reported_inclusion_count**: Count and unit; approximate counts retain qualification. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **original_taxonomy**: Original dimension/category names. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **inclusion_roster_status**: Explicit roster, partial inventory or unavailable. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **optimization_treatment**: Formal coding versus examples/discussion. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **research_guidance**: Specific recommendations attributed to authors. Rule: Do not equate full bibliography, background papers, curves and included primary studies.
- **stated_limitations**: Authors limitations, distinguished from reviewer appraisal. Rule: Do not equate full bibliography, background papers, curves and included primary studies.

## H1_hazards

- **hazard_types**: Natural/anthropogenic processes; multi-label. Rule: Multiple intensity scenarios are not multiple hazard types; physically interacting processes require demonstrated coupling.
- **hazard_source**: Observed event, design scenario, probabilistic map or generic failure. Rule: Multiple intensity scenarios are not multiple hazard types; physically interacting processes require demonstrated coupling.
- **hazard_intensity**: Magnitude/depth/velocity/return period and units. Rule: Multiple intensity scenarios are not multiple hazard types; physically interacting processes require demonstrated coupling.
- **hazard_jointness**: Separate portfolio, simultaneous, sequential, compound or cascading. Rule: Multiple intensity scenarios are not multiple hazard types; physically interacting processes require demonstrated coupling.
- **physical_hazard_model**: Actual process model and coupling. Rule: Multiple intensity scenarios are not multiple hazard types; physically interacting processes require demonstrated coupling.
- **hazard_damage_function**: Functionality/damage thresholds and validation. Rule: Multiple intensity scenarios are not multiple hazard types; physically interacting processes require demonstrated coupling.

## H2_network_flows

- **network_scale**: network scale. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **network_resolution**: network resolution. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **network_graph_direction**: network graph direction. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **network_weights**: network weights. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **od_source**: od source. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **demand_elasticity**: demand elasticity. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **flow_analysis_type**: flow analysis type. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **capacity_constraint_type**: capacity constraint type. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **queues_spillback**: queues spillback. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **transport_modes**: transport modes. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **mode_interaction**: mode interaction. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **differentiated_road_users**: differentiated road users. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **class_interaction**: class interaction. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **commodity_detail**: commodity detail. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.
- **behavioral_adaptation**: behavioral adaptation. Rule: Separate observed flows, unweighted OD routes, demand-loaded shortest paths, equilibrium/dynamic assignment and agent simulation; modes and classes are not interchangeable.

## H3_time

- **assignment_interval**: assignment interval. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.
- **event_horizon**: event horizon. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.
- **hazard_time_variation**: hazard time variation. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.
- **demand_time_variation**: demand time variation. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.
- **functionality_restoration**: functionality restoration. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.
- **repair_resource_constraints**: repair resource constraints. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.
- **restoration_validation**: restoration validation. Rule: Separate event evolution, repeated events, operational return, drying, closure snapshots, component repair and economic recovery.

## H4_consequences

- **connectivity_accessibility**: connectivity accessibility. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **transport_service_metrics**: transport service metrics. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **unmet_demand_mechanism**: unmet demand mechanism. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **physical_asset_damage**: physical asset damage. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **monetary_repair**: monetary repair. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **monetary_transport_user**: monetary transport user. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **monetary_wider_economy**: monetary wider economy. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **cargo_exposure**: cargo exposure. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **valuation_price_year**: valuation price year. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **valuation_currency**: valuation currency. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.
- **double_counting_check**: double counting check. Rule: Delay hours are not money; cargo value is not automatic loss; isolation and demand suppression are distinct; retain author-specific direct/indirect terminology separately.

## optimization

- **optimization_role**: optimization role. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **decision_maker**: decision maker. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **decision_stage**: decision stage. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **decision_variables**: decision variables. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **objective_units_weights**: objective units weights. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **constraints**: constraints. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **information_timing**: information timing. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **uncertainty_formulation**: uncertainty formulation. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **traffic_hazard_coupling**: traffic hazard coupling. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **mathematical_formulation**: mathematical formulation. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **solution_algorithm**: solution algorithm. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **problem_size**: problem size. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **runtime_hardware**: runtime hardware. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **optimality_gap_bound**: optimality gap bound. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **baseline_comparator**: baseline comparator. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **out_of_sample_policy_test**: out of sample policy test. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.
- **implementation_evidence**: implementation evidence. Rule: Do not equate inner assignment with intervention optimization, solver convergence with empirical validation, or a heuristic with global optimality.

## evidence_crosscutting

- **calibration**: calibration. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **event_validation**: event validation. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **out_of_sample_validation**: out of sample validation. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **uncertainty_type**: uncertainty type. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **sensitivity**: sensitivity. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **code_available**: code available. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **data_available**: data available. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **equity_analysis**: equity analysis. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **environmental_impacts**: environmental impacts. Rule: No universal composite quality score; appraise methods appropriate to each study design.
- **implementation_evidence**: implementation evidence. Rule: No universal composite quality score; appraise methods appropriate to each study design.

## geography

- **affiliation_country**: affiliation country. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **affiliation_counting_weight**: affiliation counting weight. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **case_country**: case country. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **case_counting_weight**: case counting weight. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **event_location**: event location. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **network_location**: network location. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **geocoding_source**: geocoding source. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **spatial_precision**: spatial precision. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.
- **stylized_network_flag**: stylized network flag. Rule: Authorship affiliation is not nationality; case location is not affiliation; fractional paper weights sum to one under each counting scheme.

## review_study_edges

- **review_id**: review id. Rule: Overlap uses eligible included studies only; missing roster is not zero membership.
- **included_study_family_id**: included study family id. Rule: Overlap uses eligible included studies only; missing roster is not zero membership.
- **included_report_id**: included report id. Rule: Overlap uses eligible included studies only; missing roster is not zero membership.
- **edge_role**: edge role. Rule: Overlap uses eligible included studies only; missing roster is not zero membership.
- **inclusion_evidence_locator**: inclusion evidence locator. Rule: Overlap uses eligible included studies only; missing roster is not zero membership.
- **roster_completeness**: roster completeness. Rule: Overlap uses eligible included studies only; missing roster is not zero membership.

## legacy_presentation

- **multiple_hazards**: multiple hazards. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **demand_loaded_od_routing**: demand loaded od routing. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **modeled_congestion**: modeled congestion. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **differentiated_road_users**: differentiated road users. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **multiple_modes**: multiple modes. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **temporal_evolution**: temporal evolution. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **functionality_restoration**: functionality restoration. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **monetary_repair**: monetary repair. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **monetary_transport_user**: monetary transport user. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
- **monetary_wider_economy**: monetary wider economy. Rule: Presentation codes inherited from v3 require calibration before conversion to finer codebook categories; not a universal sophistication score.
