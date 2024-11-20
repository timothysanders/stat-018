import numpy as np
from scipy import stats


def one_sample_z_test(
        population_mean,
        population_sd,
        sample_number,
        sample_mean,
        alpha
    ):
    sample_sigma = population_sd / np.sqrt(sample_number)
    z_statistic = (sample_mean - population_mean) / sample_sigma
    reject = False
    z_critical = np.round(stats.norm.ppf(1 - alpha / 2), 3)
    if np.abs(z_statistic) >= z_critical:
        reject = True
    d = (sample_mean - population_mean) / population_sd
    ninety_five_ci_lower = sample_mean - (sample_sigma * 1.96)
    ninety_five_ci_upper = sample_mean + (sample_sigma * 1.96)
    ninety_nine_ci_lower = sample_mean - (sample_sigma * 2.576)
    ninety_nine_ci_upper = sample_mean + (sample_sigma * 2.576)
    results = {
        "sample sigma": sample_sigma,
        "z-statistic": z_statistic,
        "reject Ho": reject,
        "d" : d,
        "95% CI": [ninety_five_ci_lower, ninety_five_ci_upper],
        "99% CI": [ninety_nine_ci_lower, ninety_nine_ci_upper]
    }
    return results


def one_sample_t_test(
        population_mean,
        sample_number,
        sample_mean,
        sample_data,
        alpha
    ):
    degrees_of_freedom = sample_number - 1
    t_critical = stats.t.ppf(1 - alpha / 2, sample_number - 1)
    sum_squares = np.sum((sample_data - sample_mean)**2)
    s_hat_x = np.sqrt(sum_squares / degrees_of_freedom)
    s_hat_x_bar = s_hat_x / np.sqrt(sample_number)
    t_statistic = (sample_mean - population_mean) / s_hat_x_bar
    reject = False
    if np.abs(t_statistic) >= t_critical:
        reject = True
    d_hat = np.abs(sample_mean - population_mean) / s_hat_x
    r_squared = t_statistic**2 / (t_statistic**2 + degrees_of_freedom)
    ninety_five_ci_lower = sample_mean - s_hat_x_bar * stats.t.ppf(1 - (0.05 / 2), degrees_of_freedom)
    ninety_five_ci_upper = sample_mean + s_hat_x_bar * stats.t.ppf(1 - (0.05 / 2), degrees_of_freedom)
    ninety_nine_ci_lower = sample_mean - s_hat_x_bar * stats.t.ppf(1 - (0.01 / 2), degrees_of_freedom)
    ninety_nine_ci_upper = sample_mean + s_hat_x_bar * stats.t.ppf(1 - (0.01 / 2), degrees_of_freedom)
    results = {
        "s_hat_x": np.round(s_hat_x, 4),
        "s_hat_x_bar": np.round(s_hat_x_bar, 4),
        "degrees of freedom": degrees_of_freedom,
        "t-statistic": np.round(t_statistic, 4),
        "t-critical": t_critical,
        "reject Ho": reject,
        "effect size (d_hat)": np.round(d_hat, 4),
        "coefficient of determination (r**2)": r_squared,
        "coefficient of non-determination (1 - r**2)": 1 - r_squared,
        "95% CI": [ninety_five_ci_lower, ninety_five_ci_upper],
        "99% CI": [ninety_nine_ci_lower, ninety_nine_ci_upper]
    }
    return results


def harmonic_mean(a, b):
    return 2 / ((1/a) + (1/b))


def two_sample_between_subjects_anova(
        treated_sample,
        untreated_sample,
        alpha
):
    treated_sample_mean = np.mean(treated_sample)
    sum_squares_treated_sample = np.sum((treated_sample - treated_sample_mean)**2)
    untreated_sample_mean = np.mean(untreated_sample)
    sum_squares_untreated_sample = np.sum((untreated_sample - untreated_sample_mean)**2)
    grand_mean = np.mean(np.concatenate((treated_sample, untreated_sample)))
    ss_between_group = (len(treated_sample) * (treated_sample_mean - grand_mean)**2) + (len(untreated_sample) * (untreated_sample_mean - grand_mean)**2)
    ss_within_group = sum_squares_treated_sample + sum_squares_untreated_sample
    df_between_group = 1
    df_within_group = (len(treated_sample) - 1) + (len(untreated_sample) - 1)
    ms_between_group = ss_between_group / df_between_group
    ms_within_group = ss_within_group / df_within_group
    f_statistic = ms_between_group / ms_within_group
    f_critical = stats.f.ppf(q=1-alpha, dfn=df_between_group, dfd=df_within_group)
    reject = False
    if np.abs(f_statistic) >= np.abs(f_critical):
        reject = True
    if len(treated_sample) == len(untreated_sample):
        n = len(treated_sample)
    else:
        n = harmonic_mean(len(treated_sample), len(untreated_sample))
    ninety_five_ci_lower = (treated_sample_mean - untreated_sample_mean) - np.sqrt(ms_within_group/n) * stats.studentized_range.ppf(1-0.05, 2, df_within_group)
    ninety_five_ci_upper = (treated_sample_mean - untreated_sample_mean) + np.sqrt(ms_within_group/n) * stats.studentized_range.ppf(1-0.05, 2, df_within_group)
    ninety_nine_ci_lower = (treated_sample_mean - untreated_sample_mean) - np.sqrt(ms_within_group/n) * stats.studentized_range.ppf(1-0.01, 2, df_within_group)
    ninety_nine_ci_upper = (treated_sample_mean - untreated_sample_mean) + np.sqrt(ms_within_group/n) * stats.studentized_range.ppf(1-0.01, 2, df_within_group)
    eta_squared = ss_between_group / (ss_between_group + ss_within_group)
    omega_squared = (ss_between_group - df_between_group * ms_within_group) / (ss_between_group + ss_within_group + ms_within_group)
    if df_within_group > 20:
        print(f"WARNING: Validate Q value from table of critical values for (2, {df_within_group}")
    results = {
        "f_statistic": f_statistic,
        "f_critical": f_critical,
        "reject": reject,
        "95% CI": [ninety_five_ci_lower, ninety_five_ci_upper],
        "99% CI": [ninety_nine_ci_lower, ninety_nine_ci_upper],
        "eta squared (biased)": eta_squared,
        "omega squared (unbiased)": omega_squared,
        "grand mean": grand_mean,
        "source table": {
            "between_group": {"ss": ss_between_group, "df": df_between_group, "ms": ms_between_group},
            "within_group": {"ss": ss_within_group, "df": df_within_group, "ms": ms_within_group}
        }
    }
    return results


def two_sample_within_subjects_anova(
        treated_sample,
        untreated_sample,
        alpha
):
    treated_sample_mean = np.mean(treated_sample)
    sum_squares_treated_sample = np.sum((treated_sample - treated_sample_mean)**2)
    untreated_sample_mean = np.mean(untreated_sample)
    sum_squares_untreated_sample = np.sum((untreated_sample - untreated_sample_mean)**2)
    grand_mean = np.mean(np.concatenate((treated_sample, untreated_sample)))
    person_mean = (treated_sample + untreated_sample) / 2
    ss_between_group = (len(treated_sample) * (treated_sample_mean - grand_mean)**2) + (len(untreated_sample) * (untreated_sample_mean - grand_mean)**2)
    ss_within_group = sum_squares_treated_sample + sum_squares_untreated_sample
    ss_between_people = np.sum(2 * (person_mean - grand_mean)**2)
    ss_true_error = ss_within_group - ss_between_people
    df_between_group = 1
    df_within_group = (len(treated_sample) - 1) + (len(untreated_sample) - 1)
    df_between_people = len(treated_sample) - 1
    df_true_error = df_within_group - df_between_people
    ms_between_group = ss_between_group / df_between_group
    ms_true_error = ss_true_error / df_true_error
    f_statistic = ms_between_group / ms_true_error
    f_critical = stats.f.ppf(q=1-alpha, dfn=df_between_group, dfd=df_true_error)
    reject = False
    if np.abs(f_statistic) >= np.abs(f_critical):
        reject = True
    if len(treated_sample) == len(untreated_sample):
        n = len(treated_sample)
    else:
        n = harmonic_mean(len(treated_sample), len(untreated_sample))
    ninety_five_ci_lower = (treated_sample_mean - untreated_sample_mean) - np.sqrt(ms_true_error/n) * stats.studentized_range.ppf(1-0.05, 2, df_true_error)
    ninety_five_ci_upper = (treated_sample_mean - untreated_sample_mean) + np.sqrt(ms_true_error/n) * stats.studentized_range.ppf(1-0.05, 2, df_true_error)
    ninety_nine_ci_lower = (treated_sample_mean - untreated_sample_mean) - np.sqrt(ms_true_error/n) * stats.studentized_range.ppf(1-0.01, 2, df_true_error)
    ninety_nine_ci_upper = (treated_sample_mean - untreated_sample_mean) + np.sqrt(ms_true_error/n) * stats.studentized_range.ppf(1-0.01, 2, df_true_error)
    eta_squared = ss_between_group / (ss_between_group + ss_true_error)
    omega_squared = (ss_between_group - (df_between_group * ms_true_error)) / (ss_between_group + ss_true_error + ms_true_error)
    results = {
        "f_statistic": f_statistic,
        "f_critical": f_critical,
        "reject": reject,
        "95% CI": [ninety_five_ci_lower, ninety_five_ci_upper],
        "99% CI": [ninety_nine_ci_lower, ninety_nine_ci_upper],
        "eta squared (biased)": eta_squared,
        "omega squared (unbiased)": omega_squared,
        "grand mean": grand_mean,
        "source table": {
            "between_group": {"ss": ss_between_group, "df": df_between_group, "ms": ms_between_group},
            "within_group": {"ss": ss_within_group, "df": df_within_group},
            "between_people": {"ss": ss_between_people, "df": df_between_people},
            "true_error": {"ss": ss_true_error, "df": df_true_error, "ms": ms_true_error}
        }
    }
    return results