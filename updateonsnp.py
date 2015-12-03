def update(read, ref, prior, popprob, notes, debug=False, error_rate=0.15):
    if ref[0]==ref[1]: # homozygous case
        if read==ref[0]: # match
            p_obs_given_match = 1
            notes['homohit'] += 1
        else:
            p_obs_given_match = error_rate
            notes['homomiss'] += 1
        p_obs_given_mismatch = popprob
    else: # heterozygous
        if read in ref:
            p_obs_given_match = 0.5
            notes['heterohit'] += 1
        else:
            p_obs_given_match = error_rate
            notes['heteromiss'] += 1
        p_obs_given_mismatch = popprob
        if popprob>.5:
            notes['hetcom'] += 1
        else:
            notes['hetrare'] += 1
    p_obs = prior*p_obs_given_match + (1-prior)*p_obs_given_mismatch
    posterior = prior * p_obs_given_match / p_obs
    print 'Updating on "%s"?="%s" prior=%f p(obs|him)=%f p(obs|~him)=%f p(obs)=%f posterior=%f' % (read,ref,prior,p_obs_given_match,p_obs_given_mismatch,p_obs,posterior)
    return posterior
