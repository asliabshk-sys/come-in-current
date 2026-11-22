# SEC-03 / SEC-04 candidate checkpoint

Only isolated candidate files are written under this folder. Protected application source is untouched by this workstream. Baseline server SHA-25670f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07. Planned:strict trusted-proxy client identity,atomicIP+subject reservation/release using existingtransaction helper,preserve login failed-onlycounts. Next:write candidate;execute same before/after isolatedtests with real localhostMongoDB. No provider/native/production operations.

Initial before-harness attempt saved9PASS/15FAIL/2ERROR. TwoERRORsarefixture-only:generatedemailcontaineduppercaseT/Z,butactual loginnormalizeslowercase beforelookup. Correctedv2fixturecanonicalizationonly;all26assertionspreserved. Originalrunner/results/logsretained. Next:executev2before/afterintoverified-run/. Actualproductionfilesuntouched.

Corrected26-caseharness:before11PASS15FAIL,initialcandidateafter26PASS0FAIL. Review found initialcandidatecancreateemptynewsubjectdocswhenIPalreadycapped;stronger no-rejected-bucket-write invariant added beforemerge. Initialcandidatebytes andall26caseevidence preserved. Finalcandidate moves conditionalcappedupserts inside transaction;post-duplicatefreshcount onlyclassifiesrejection/initial-insertrace,neveradmits. Next:27casebefore/finalafterregression withnew outputnamespace.
