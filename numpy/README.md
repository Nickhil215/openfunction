# numpy FastAPI Service

Auto-generated FastAPI service for numpy functions with high-performance JSON serialization using orjson.

## Features
- **High Performance**: Uses orjson for faster JSON serialization/deserialization
- **Auto-generated endpoints**: Individual endpoints for each function
- **Batch processing**: Execute multiple functions in a single request
- **Docker support**: Ready-to-deploy Docker container
- **Interactive docs**: Built-in Swagger UI documentation

## Functions Available:
- `test_reveal` (ID: 41aad374-b32e-4fb8-a908-ca3af446b356): Validate that mypy correctly infers the return-types of
the expressions in `path`.
- `test_pass` (ID: 5db9858d-dfbf-4d24-a6e4-5276cfeed96e): No description
- `test_code_runs` (ID: 1cfbf2d3-25a1-47f0-aa84-af21a289a7e7): Validate that the code in `path` properly during runtime.
- `strip_func` (ID: eed6c6c1-7a97-4284-ba70-44bfd1c32af2): `re.sub` helper function for stripping module names.
- `run_mypy` (ID: ce493dc2-253b-4a5f-9d6e-d269b51d77b7): Clears the cache and run mypy before running any of the typing tests.

The mypy results are cached in `OUTPUT_MYPY` for further use.

The cache refresh can be skipped using

NUMPY_TYPING_TEST_CLEAR_CACHE=0 pytest numpy/typing/tests
- `get_test_cases` (ID: c9dcabe9-1b3d-43ea-ae8e-52ad789f0ca1): No description
- `test_keys` (ID: 6b8d7759-ffb2-4279-add7-45b3b24e90c6): Test that ``TYPES.keys()`` and ``numpy.typing.__all__`` are synced.
- `test_get_type_hints_str` (ID: be3a44c1-0dd9-4cf1-83f8-788f2ba06a74): Test `typing.get_type_hints` with string-representation of types.
- `test_get_type_hints` (ID: f5943bc9-7f2c-4429-908c-77a90ac7ebc3): Test `typing.get_type_hints`.
- `test_get_origin` (ID: 5b53cb10-7c08-4f26-895b-e87b1518eb9f): Test `typing.get_origin`.
- `test_get_args` (ID: 96a7d0f4-664a-4eb9-b3ba-cf65fc255abd): Test `typing.get_args`.
- `plugin` (ID: 8441740d-952b-4ffd-97d6-46692ae5c4e2): No description
- `test_warning_calls` (ID: 747bc4a2-cd31-4285-b7a6-afcdb5ae6454): No description
- `test_pep338` (ID: be344441-955b-47ea-bf21-ca1b15c1548a): No description
- `test_f2py` (ID: 1174b696-d6d5-4d39-a8d1-8d76d48e962d): No description
- `find_f2py_commands` (ID: 8c716ecf-3e1c-4c76-b541-97b4c7e7c28a): No description
- `test_numpy_reloading` (ID: 87040f1f-b8d1-46d5-bab5-7df5034dc354): No description
- `test_novalue` (ID: d506adf4-0ba2-400e-b243-22807cad89eb): No description
- `test_full_reimport` (ID: c073fc26-7031-4006-b35a-c613da390d73): No description
- `test_numpy_namespace` (ID: 59cc94a1-df90-47a2-96f6-06d10c75dcc2): No description
- `test_numpy_linalg` (ID: 48c382db-b8b0-4bf5-adae-0818c1e857f9): No description
- `test_numpy_fft` (ID: 8c7d0866-c8f4-4c13-aca1-c41eca83ac3c): No description
- `test_main_namespace_all_dir_coherence` (ID: fa129e3b-cf38-4dc4-b8fb-ca47e1763a13): Checks if `dir(np)` and `np.__all__` are consistent and return
the same content, excluding exceptions and private members.
- `test_import_lazy_import` (ID: 7f4eed1a-d230-4500-93c4-14d019c6dbbc): Make sure we can actually use the modules we lazy load.

While not exported as part of the public API, it was accessible.  With the
use of __getattr__ and __dir__, this isn't always true It can happen that
an infinite recursion may happen.

This is the only way I found that would force the failure to appear on the
badly implemented code.

We also test for the presence of the lazily imported modules in dir
- `test_functions_single_location` (ID: 14143f66-3487-4883-aad0-b00caf3a687b): Check that each public function is available from one location only.

Test performs BFS search traversing NumPy's public API. It flags
any function-like object that is accessible from more that one place.
- `test_dir_testing` (ID: 97e52d8d-899d-4599-bfc8-0b1cb2c73a84): Assert that output of dir has only one "testing/tester"
attribute without duplicate
- `test_core_shims_coherence` (ID: b132e845-88f0-4095-962a-a9576f8dddd9): Check that all "semi-public" members of `numpy._core` are also accessible
from `numpy.core` shims.
- `test_array_api_entry_point` (ID: a7a765e9-5145-4219-a460-db861e0a0f0f): Entry point for Array API implementation can be found with importlib and
returns the main numpy namespace.
- `test_api_importable` (ID: 7b565104-08c9-455c-aafd-ac1db9c7f812): Check that all submodules listed higher up in this file can be imported

Note that if a PRIVATE_BUT_PRESENT_MODULES entry goes missing, it may
simply need to be removed from the list (deprecation may or may not be
needed - apply common sense).
- `test_all_modules_are_expected_2` (ID: d4b196b5-2ada-4a88-b685-72a090a747c5): Method checking all objects. The pkgutil-based method in
`test_all_modules_are_expected` does not catch imports into a namespace,
only filenames.  So this test is more thorough, and checks this like:

    import .lib.scimath as emath

To check if something in a module is (effectively) public, one can check if
there's anything in that namespace that's a public function/object but is
not exposed in a higher-level namespace.  For example for a `numpy.lib`
submodule::

    mod = np.lib.mixins
    for obj in mod.__all__:
        if obj in np.__all__:
            continue
        elif obj in np.lib.__all__:
            continue

        else:
            print(obj)
- `test_all_modules_are_expected` (ID: 5fccdb34-d089-489e-bf9d-bba3e7ec6b6c): Test that we don't add anything that looks like a new public module by
accident.  Check is based on filenames.
- `test___qualname___and___module___attribute` (ID: c62098f7-00b3-47a2-9d7c-a2042d84a5eb): No description
- `test___module___attribute` (ID: 3a7f81b8-a7c5-4dc2-b824-1eecd015a347): No description
- `test_NPY_NO_EXPORT` (ID: 66b9d9fd-d42c-4e83-ba76-8e6d308201ad): No description
- `is_unexpected` (ID: 07542fbd-56a9-419b-a7eb-7225039e933e): Check if this needs to be considered.
- `check_dir` (ID: d24d29e3-7e93-4add-b075-b55275c82235): Returns a mapping of all objects with the wrong __module__ attribute.
- `test_version_module` (ID: 615a56c0-e4c6-4059-bb86-56215d26f20c): No description
- `test_valid_numpy_version` (ID: 9eb50620-ff69-491f-99e9-faec15dfb929): No description
- `test_short_version` (ID: 54f417f0-4145-4470-a053-79447d7b0b25): No description
- `test_zeros` (ID: db63df59-92d2-4238-964d-0c6606ab8ad4): No description
- `test_repmat` (ID: 9856e2e4-10fb-479d-b35c-5bb583cf7a3e): No description
- `test_randn` (ID: 61b14e95-4913-40db-b1e3-740ff356c921): No description
- `test_rand` (ID: d637ec32-cd5a-4a75-a4b6-168a52b8972b): No description
- `test_ones` (ID: 8692771c-2b6d-4fe9-bded-20e1b402088a): No description
- `test_identity` (ID: ae232b10-e6c2-434b-9aed-a981e2029c6a): No description
- `test_eye` (ID: ace470f5-ba73-42d9-b57f-7eec7cf333da): No description
- `test_empty` (ID: 4c6eddae-409a-40da-9c53-460d3e3f3a3a): No description
- `test_lazy_load` (ID: 9005cc93-6239-4956-93e3-dcf14136dcb2): No description
- `test_pkg_config_entrypoint` (ID: 8f53df62-4234-4575-8533-61f03570023e): No description
- `test_pkg_config_config_exists` (ID: 843aff8d-7fab-4db0-93a4-0ad4c839420b): No description
- `test_no_duplicates_in_np__all__` (ID: ab36d1a2-a32d-4f75-b903-c4606513d390): No description
- `test_warn_len_equal_call_scenarios` (ID: e4e72621-02fd-425f-90d5-aabbaa0c4432): No description
- `test_temppath` (ID: d314e090-421a-40eb-95a6-a1e6a7ea388a): No description
- `test_tempdir` (ID: 7a763d63-84fc-4da0-99cf-47893f7b5988): No description
- `test_suppress_warnings_type` (ID: ad581be9-43e5-4106-8628-6bfa9c2fd9e9): No description
- `test_suppress_warnings_record` (ID: df6330f5-a567-423d-b830-2171c3e07d5e): No description
- `test_suppress_warnings_module` (ID: 3db46194-2411-4a30-99ef-343755321a7e): No description
- `test_suppress_warnings_forwarding` (ID: f9101842-4ca0-48a4-9e16-3f4f3d907202): No description
- `test_suppress_warnings_decorate_no_record` (ID: 86921f8d-bbee-403c-82c5-6b8b8b2d8b7a): No description
- `test_clear_and_catch_warnings_inherit` (ID: 6708a3c5-a036-429f-bac1-7d15d5ba74d6): No description
- `test_clear_and_catch_warnings` (ID: 3a655698-ee5e-4691-bb72-c725f378d7c8): No description
- `assert_warn_len_equal` (ID: 601889aa-bb1a-4d07-8dc6-d30cd5d2340a): No description
- `print_new_cast_table` (ID: e82be433-c9a8-42ff-85d1-918486c003e8): Prints new casts, the values given are default "can-cast" values, not
actual ones.
- `print_coercion_table` (ID: bbb2d824-8282-419b-8d4d-12047340e11f): No description
- `print_cancast_table` (ID: df02a06e-226f-4e67-93a2-40004486cbbf): No description
- `get_overridable_numpy_ufuncs` (ID: 74e2e070-c46b-4a5c-9388-de7e7d79be30): List all numpy ufuncs overridable via `__array_ufunc__`

Parameters
----------
None

Returns
-------
set
    A set containing all overridable ufuncs in the public numpy API.
- `get_overridable_numpy_array_functions` (ID: 3312da61-6578-49c7-8f35-fa84202ee377): List all numpy functions overridable via `__array_function__`

Parameters
----------
None

Returns
-------
set
    A set containing all functions in the public numpy API that are
    overridable via `__array_function__`.
- `allows_array_ufunc_override` (ID: 7ec32fb5-e1ad-407e-afce-c9374bea8a7c): Determine if a function can be overridden via `__array_ufunc__`

Parameters
----------
func : callable
    Function that may be overridable via `__array_ufunc__`

Returns
-------
bool
    `True` if `func` is overridable via `__array_ufunc__` and
    `False` otherwise.

Notes
-----
This function is equivalent to ``isinstance(func, np.ufunc)`` and
will work correctly for ufuncs defined outside of Numpy.
- `allows_array_function_override` (ID: 6ea19969-efb8-4c68-a7f6-00791b754cc6): Determine if a Numpy function can be overridden via `__array_function__`

Parameters
----------
func : callable
    Function that may be overridable via `__array_function__`

Returns
-------
bool
    `True` if `func` is a function in the Numpy API that is
    overridable via `__array_function__` and `False` otherwise.
- `warmup` (ID: f8511d57-b2ae-40a9-abce-09af9befe9c4): No description
- `params_1` (ID: 92b85c65-fc08-4ba3-b8cb-dc346f65d19a): No description
- `params_0` (ID: 2fe1a966-c884-4335-b277-559b2ed54cdb): No description
- `dtype` (ID: 5c68ec2f-9004-43da-bf3e-6d6d536fb8ed): No description
- `comp_state` (ID: 4015f10d-3a11-4d3c-b465-c1130941682e): No description
- `test_zero_padding` (ID: 301691c7-f84f-439a-ab75-c5c5c5ab4b5d): Ensure that the implicit zero-padding does not cause problems.
- `test_reference_data` (ID: a628557c-7282-4df2-9ac2-568738a84b43): Check that SeedSequence generates data the same as the C++ reference.

https://gist.github.com/imneme/540829265469e673d045
- `test_multinomial_empty` (ID: 1fd582a2-dfbb-4e52-9fb5-bade8bb5077f): No description
- `test_multinomial_1d_pval` (ID: 307695b3-0c26-4aa8-83bb-f35f67f45e5f): No description
- `test_swapped_singleton_against_direct` (ID: b7dd00ff-4118-432f-b6e1-66aa11508c07): No description
- `test_swap_worked` (ID: 5c2756cd-6b98-4003-bfdc-97ecf8e209b3): No description
- `test_state_error_alt_bit_gen` (ID: e79e3d3d-9daf-4da0-83f8-be646e725042): No description
- `test_seed_alt_bit_gen` (ID: 996e424c-cc16-4287-b894-579e12b92e34): No description
- `test_randomstate_ctor_old_style_pickle` (ID: 8388ad7f-2eca-42ff-8892-bfa3d8ae5c2a): No description
- `test_integer_repeat` (ID: ca5cc9ed-17b3-41c9-bc84-daa75480f483): No description
- `test_integer_dtype` (ID: d12c1542-7e87-4177-b56d-e41dd9133a98): No description
- `test_hot_swap` (ID: d77d02de-0b15-4812-9eb0-4bc424424199): No description
- `test_broadcast_size_error` (ID: 50742fbc-0e5b-4839-a415-d95417338908): No description
- `restore_singleton_bitgen` (ID: 30e2b3e3-0564-4150-b567-132d7661661d): Ensures that the singleton bitgen is restored after a test
- `int_func` (ID: 998cd410-fd67-4287-a2d9-1c4d00f6ca24): No description
- `assert_mt19937_state_equal` (ID: 44832c9e-7992-411c-a565-4f9070a64eb7): No description
- `test_single_arg_integer_exception` (ID: ca4a086a-68c0-4596-a85d-8e9325123bf3): No description
- `test_ragged_shuffle` (ID: ab3586b8-68de-4c75-b8c6-7286d9df9669): No description
- `test_pickle_preserves_seed_sequence` (ID: 70f41aa6-c26e-408d-a04d-03cc98ac476d): No description
- `test_legacy_pickle` (ID: a7f3e0fa-e447-49ba-bfa9-e48080eaf5ad): No description
- `test_jumped` (ID: 5fc24a74-e955-4a7e-b7ad-5a961318f3fe): No description
- `test_generator_ctor_old_style_pickle` (ID: 7e1a2f22-d70b-4795-bef1-7b5a148c71ca): No description
- `test_contig_req_out` (ID: 87cd5a88-b766-4a89-b151-0ca5bc909d1a): No description
- `test_c_contig_req_out` (ID: d262d6c2-db2c-438b-8bc1-f3f90cc944b3): No description
- `test_broadcast_size_scalar` (ID: 319e63bd-4776-4bcf-ad1d-6683996363ed): No description
- `test_broadcast_size_error` (ID: db909f4e-ef52-48f1-be20-711b8130f8fe): No description
- `endpoint` (ID: f33dd48c-ae6e-4cf7-89ea-6bf92443ae33): No description
- `test_numba` (ID: 80b9b202-a228-4547-b225-22f492ce3331): No description
- `test_cython` (ID: e1bc7575-d710-48c3-817a-2fd5e60d78cb): No description
- `test_cffi` (ID: aa897075-44ad-4819-8616-b053cec37084): No description
- `uniform_from_uint64` (ID: cab4343f-c4fc-4a41-90a9-ae779fe6af23): No description
- `uniform_from_uint32` (ID: c79b329d-7604-4ae1-9878-caab15f98b56): No description
- `uniform_from_uint` (ID: df18c780-aff9-4f7f-b4bc-771f223b3fec): No description
- `uniform_from_dsfmt` (ID: 4577242a-23e8-4eb5-a9e7-99d5f72335f1): No description
- `uniform32_from_uint64` (ID: 4c29b749-8b93-4ec9-a869-cbfcdfec6f93): No description
- `uniform32_from_uint53` (ID: 8a63dd5b-e3b3-459e-8c6b-d7ca4b21c39b): No description
- `uniform32_from_uint32` (ID: 3f0fbea8-553c-4060-8c7c-b47d1c4ece78): No description
- `uniform32_from_uint` (ID: 60c9650e-5453-4e9a-b139-a097d7ffdd2d): No description
- `uint32_to_float32` (ID: 2b031245-357e-4c8d-93a3-b49aab37c209): No description
- `test_seedsequence` (ID: 54e64d3a-67e9-4318-a910-4e9d2d725c8a): No description
- `test_non_spawnable` (ID: 7ca242ea-d231-48f1-b84f-92caf61040c6): No description
- `test_generator_spawning` (ID: 6fa2fbbd-b495-4622-9246-8b6383b6b3bc): Test spawning new generators and bit_generators directly.
- `gauss_from_uint` (ID: 885f4fe9-517d-4c8b-9c49-4e151c57c9fb): No description
- `assert_state_equal` (ID: 3d401fa2-bef1-4f65-8c5e-005b3826e534): No description
- `set_bit_generator` (ID: ef0a0359-5d9b-4bf4-a9cd-f26ee0d28baa): No description
- `get_bit_generator` (ID: cf327e57-783e-4138-87b7-816d9c4799ee): No description
- `test_identity` (ID: 26ffb037-b0fa-444e-8650-745aab5a7bec): No description
- `test_froomroots` (ID: ed733393-a3e9-43cc-81c2-8ea95a4ce89a): No description
- `test_fit` (ID: 2f767eb3-895f-419f-bf97-5bbde6d6501f): No description
- `test_composition` (ID: 538c5c2a-5e9b-4b97-85be-418926932581): No description
- `test_basis` (ID: 0e6a613a-3780-4358-a330-4024902b6e07): No description
- `test_symbol` (ID: 6d3db82b-82bc-4480-8b96-a9686698ed27): No description
- `test_set_default_printoptions` (ID: d267a51c-c57c-4fc4-87d4-82ff9028c3db): No description
- `test_numeric_object_coefficients` (ID: 63730a57-40f2-466b-9943-a610cc21ac29): No description
- `test_nonnumeric_object_coefficients` (ID: 9d474e9a-3deb-496b-b320-dc1b68d12b04): Test coef fallback for object arrays of non-numeric coefficients.
- `test_complex_coefficients` (ID: 60376320-1deb-43c9-908e-3c61bda92d8a): Test both numpy and built-in complex.
- `trim` (ID: 83cfaf59-037d-4f65-aea4-12e627cf4501): No description
- `test_polyval2d_array_function_hook` (ID: 7fddf308-0f15-4e86-b55b-d59c8abe0b2c): No description
- `test_polygrid2d_array_function_hook` (ID: 2b80abcf-ac18-4a53-ab09-00d2a97bd02e): No description
- `trim` (ID: b7d0d17c-e63e-4eef-aff5-6ce20c34df53): No description
- `trim` (ID: 9f53adac-3057-47fb-9a0a-cbc11171558c): No description
- `trim` (ID: ae911a4d-c737-4d2e-bf87-73494dd44560): No description
- `trim` (ID: 0a984cb6-a7b4-4e1c-8f38-2e004f23ca37): No description
- `test_ufunc_override` (ID: 8873d068-82b2-430b-9a19-a910c5ab6ef2): No description
- `test_truncate` (ID: 0716c5e4-014a-446a-b40e-fa9a7d7db913): No description
- `test_truediv` (ID: 64696981-3841-46e3-8d0c-525b7377e558): No description
- `test_trim` (ID: 69c62baa-5513-48b9-b8db-be6df6b63bc5): No description
- `test_sub` (ID: 29d4fbf0-40bc-4e0f-b1a5-8d8625ddba7a): No description
- `test_roots` (ID: 0d8a4a34-b840-4ae6-b058-6d678578b09c): No description
- `test_pow` (ID: 9078347d-18f1-4a7b-b6ec-2584877a3f17): No description
- `test_not_equal` (ID: 0cb9f9e9-4a51-44e5-a3d6-1250db5fce9b): No description
- `test_mul` (ID: 58b56c83-d758-4885-b450-67d9704eb2cd): No description
- `test_mod` (ID: 7b1467de-b708-4ec0-9969-decd6fac1551): No description
- `test_mapparms` (ID: 0b20667d-0230-41ea-9575-c0dfa68e0cbf): No description
- `test_linspace` (ID: ba3d3970-b075-44af-8f4b-601c53fad546): No description
- `test_integ` (ID: 6fcf4299-9fdd-41dd-a17b-c0e5cea66910): No description
- `test_identity` (ID: 85704d47-1a1d-412b-b080-f0d4189eda9e): No description
- `test_fromroots` (ID: f8de8ed4-e304-4400-824c-652bb301b802): No description
- `test_floordiv` (ID: 08ef6592-9b81-4efb-ae75-607fdfad7ce1): No description
- `test_fit` (ID: 72d8929f-f691-45b9-b53e-5158f00b8d58): No description
- `test_equal` (ID: 4d283e0e-adeb-40ad-8a01-6135e46cf751): No description
- `test_divmod` (ID: 7e3cb65d-a991-444e-82ba-79e843492269): No description
- `test_deriv` (ID: 7c3d4124-bfce-4992-ad09-2adfe5a4d190): No description
- `test_degree` (ID: 67787418-d7d1-4fb2-b557-a69b4b8f0915): No description
- `test_cutdeg` (ID: 4d2ed992-008f-49a6-a862-40a16542fdba): No description
- `test_copy` (ID: 179490de-ed12-4140-ac39-bdcd3e8c3999): No description
- `test_conversion` (ID: 80b3a4b5-ac08-4408-af95-98595c92af05): No description
- `test_cast` (ID: 3a392c20-7b6d-4aa5-8520-b0fdd0b9b5d0): No description
- `test_call_with_list` (ID: 97d883e3-a809-42d2-90ad-28b5613d4cbb): No description
- `test_call` (ID: 1a3e24d0-d8f5-4fed-bb69-a927957efcc7): No description
- `test_basis` (ID: e01791f9-bd06-4fbd-b31d-b5435afb36fb): No description
- `test_bad_conditioned_fit` (ID: fb5fdaf6-53f3-43cf-b8a7-68e6064b1e1b): No description
- `test_add` (ID: a7bc79fc-27aa-4071-a1e3-7ed06613d4b6): No description
- `assert_poly_almost_equal` (ID: 1542d7b9-7fab-4d92-9134-c94a24d60f12): No description
- `Poly` (ID: 33896bb1-b1e4-4305-a8f6-3e7b2a69b73f): No description
- `trim` (ID: 18b4fe45-0086-4e41-bd41-c162cbba6968): No description
- `set_default_printstyle` (ID: 20969d4e-6b49-477c-aedc-9a3785a7f12e): Set the default format for the string representation of polynomials.

Values for ``style`` must be valid inputs to ``__format__``, i.e. 'ascii'
or 'unicode'.

Parameters
----------
style : str
    Format string for default printing style. Must be either 'ascii' or
    'unicode'.

Notes
-----
The default format depends on the platform: 'unicode' is used on
Unix-based systems and 'ascii' on Windows. This determination is based on
default font support for the unicode superscript and subscript ranges.

Examples
--------
>>> p = np.polynomial.Polynomial([1, 2, 3])
>>> c = np.polynomial.Chebyshev([1, 2, 3])
>>> np.polynomial.set_default_printstyle('unicode')
>>> print(p)
1.0 + 2.0·x + 3.0·x²
>>> print(c)
1.0 + 2.0·T₁(x) + 3.0·T₂(x)
>>> np.polynomial.set_default_printstyle('ascii')
>>> print(p)
1.0 + 2.0 x + 3.0 x**2
>>> print(c)
1.0 + 2.0 T_1(x) + 3.0 T_2(x)
>>> # Formatting supersedes all class/package-level defaults
>>> print(f"{p:unicode}")
1.0 + 2.0·x + 3.0·x²
- `trimseq` (ID: 7709da89-4a19-4537-a288-359548d400fa): Remove small Poly series coefficients.

Parameters
----------
seq : sequence
    Sequence of Poly series coefficients.

Returns
-------
series : sequence
    Subsequence with trailing zeros removed. If the resulting sequence
    would be empty, return the first element. The returned sequence may
    or may not be a view.

Notes
-----
Do not lose the type info if the sequence contains unknown objects.
- `trimcoef` (ID: 3392c98b-c629-4326-a8a6-14e163a8a207): Remove "small" "trailing" coefficients from a polynomial.

"Small" means "small in absolute value" and is controlled by the
parameter `tol`; "trailing" means highest order coefficient(s), e.g., in
``[0, 1, 1, 0, 0]`` (which represents ``0 + x + x**2 + 0*x**3 + 0*x**4``)
both the 3-rd and 4-th order coefficients would be "trimmed."

Parameters
----------
c : array_like
    1-d array of coefficients, ordered from lowest order to highest.
tol : number, optional
    Trailing (i.e., highest order) elements with absolute value less
    than or equal to `tol` (default value is zero) are removed.

Returns
-------
trimmed : ndarray
    1-d array with trailing zeros removed.  If the resulting series
    would be empty, a series containing a single zero is returned.

Raises
------
ValueError
    If `tol` < 0

Examples
--------
>>> from numpy.polynomial import polyutils as pu
>>> pu.trimcoef((0,0,3,0,5,0,0))
array([0.,  0.,  3.,  0.,  5.])
>>> pu.trimcoef((0,0,1e-3,0,1e-5,0,0),1e-3) # item == tol is trimmed
array([0.])
>>> i = complex(0,1) # works for complex
>>> pu.trimcoef((3e-4,1e-3*(1-i),5e-4,2e-5*(1+i)), 1e-3)
array([0.0003+0.j   , 0.001 -0.001j])
- `mapparms` (ID: 7971ef60-1e6c-42cf-8a56-68f0162d3f41): Linear map parameters between domains.

Return the parameters of the linear map ``offset + scale*x`` that maps
`old` to `new` such that ``old[i] -> new[i]``, ``i = 0, 1``.

Parameters
----------
old, new : array_like
    Domains. Each domain must (successfully) convert to a 1-d array
    containing precisely two values.

Returns
-------
offset, scale : scalars
    The map ``L(x) = offset + scale*x`` maps the first domain to the
    second.

See Also
--------
getdomain, mapdomain

Notes
-----
Also works for complex numbers, and thus can be used to calculate the
parameters required to map any line in the complex plane to any other
line therein.

Examples
--------
>>> from numpy.polynomial import polyutils as pu
>>> pu.mapparms((-1,1),(-1,1))
(0.0, 1.0)
>>> pu.mapparms((1,-1),(-1,1))
(-0.0, -1.0)
>>> i = complex(0,1)
>>> pu.mapparms((-i,-1),(1,i))
((1+1j), (1-0j))
- `mapdomain` (ID: 0c038367-4ee4-42b6-b46f-52b7456e4501): Apply linear map to input points.

The linear map ``offset + scale*x`` that maps the domain `old` to
the domain `new` is applied to the points `x`.

Parameters
----------
x : array_like
    Points to be mapped. If `x` is a subtype of ndarray the subtype
    will be preserved.
old, new : array_like
    The two domains that determine the map.  Each must (successfully)
    convert to 1-d arrays containing precisely two values.

Returns
-------
x_out : ndarray
    Array of points of the same shape as `x`, after application of the
    linear map between the two domains.

See Also
--------
getdomain, mapparms

Notes
-----
Effectively, this implements:

.. math::
    x\_out = new[0] + m(x - old[0])

where

.. math::
    m = \frac{new[1]-new[0]}{old[1]-old[0]}

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial import polyutils as pu
>>> old_domain = (-1,1)
>>> new_domain = (0,2*np.pi)
>>> x = np.linspace(-1,1,6); x
array([-1. , -0.6, -0.2,  0.2,  0.6,  1. ])
>>> x_out = pu.mapdomain(x, old_domain, new_domain); x_out
array([ 0.        ,  1.25663706,  2.51327412,  3.76991118,  5.02654825, # may vary
        6.28318531])
>>> x - pu.mapdomain(x_out, new_domain, old_domain)
array([0., 0., 0., 0., 0., 0.])

Also works for complex numbers (and thus can be used to map any line in
the complex plane to any other line therein).

>>> i = complex(0,1)
>>> old = (-1 - i, 1 + i)
>>> new = (-1 + i, 1 - i)
>>> z = np.linspace(old[0], old[1], 6); z
array([-1. -1.j , -0.6-0.6j, -0.2-0.2j,  0.2+0.2j,  0.6+0.6j,  1. +1.j ])
>>> new_z = pu.mapdomain(z, old, new); new_z
array([-1.0+1.j , -0.6+0.6j, -0.2+0.2j,  0.2-0.2j,  0.6-0.6j,  1.0-1.j ]) # may vary
- `getdomain` (ID: e5251181-90f5-43ea-9c62-676ddb33185d): Return a domain suitable for given abscissae.

Find a domain suitable for a polynomial or Chebyshev series
defined at the values supplied.

Parameters
----------
x : array_like
    1-d array of abscissae whose domain will be determined.

Returns
-------
domain : ndarray
    1-d array containing two values.  If the inputs are complex, then
    the two returned points are the lower left and upper right corners
    of the smallest rectangle (aligned with the axes) in the complex
    plane containing the points `x`. If the inputs are real, then the
    two points are the ends of the smallest interval containing the
    points `x`.

See Also
--------
mapparms, mapdomain

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial import polyutils as pu
>>> points = np.arange(4)**2 - 5; points
array([-5, -4, -1,  4])
>>> pu.getdomain(points)
array([-5.,  4.])
>>> c = np.exp(complex(0,1)*np.pi*np.arange(12)/6) # unit circle
>>> pu.getdomain(c)
array([-1.-1.j,  1.+1.j])
- `format_float` (ID: af1fbb82-8249-4a20-ba37-0d2969e7ab64): No description
- `as_series` (ID: 899c71c2-96d8-4513-a517-2c4a5fa32587): Return argument as a list of 1-d arrays.

The returned list contains array(s) of dtype double, complex double, or
object.  A 1-d argument of shape ``(N,)`` is parsed into ``N`` arrays of
size one; a 2-d argument of shape ``(M,N)`` is parsed into ``M`` arrays
of size ``N`` (i.e., is "parsed by row"); and a higher dimensional array
raises a Value Error if it is not first reshaped into either a 1-d or 2-d
array.

Parameters
----------
alist : array_like
    A 1- or 2-d array_like
trim : boolean, optional
    When True, trailing zeros are removed from the inputs.
    When False, the inputs are passed through intact.

Returns
-------
[a1, a2,...] : list of 1-D arrays
    A copy of the input data as a list of 1-d arrays.

Raises
------
ValueError
    Raised when `as_series` cannot convert its input to 1-d arrays, or at
    least one of the resulting arrays is empty.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial import polyutils as pu
>>> a = np.arange(4)
>>> pu.as_series(a)
[array([0.]), array([1.]), array([2.]), array([3.])]
>>> b = np.arange(6).reshape((2,3))
>>> pu.as_series(b)
[array([0., 1., 2.]), array([3., 4., 5.])]

>>> pu.as_series((1, np.arange(3), np.arange(2, dtype=np.float16)))
[array([1.]), array([0., 1., 2.]), array([0., 1.])]

>>> pu.as_series([2, [1.1, 0.]])
[array([2.]), array([1.1])]

>>> pu.as_series([2, [1.1, 0.]], trim=False)
[array([2.]), array([1.1, 0. ])]
- `polyvander3d` (ID: 0d58b319-f137-43ae-9354-32ff45b97266): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y, z)``. If `l`, `m`, `n` are the given degrees in `x`, `y`, `z`,
then The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (m+1)(n+1)i + (n+1)j + k] = x^i * y^j * z^k,

where ``0 <= i <= l``, ``0 <= j <= m``, and ``0 <= j <= n``.  The leading
indices of `V` index the points ``(x, y, z)`` and the last index encodes
the powers of `x`, `y`, and `z`.

If ``V = polyvander3d(x, y, z, [xdeg, ydeg, zdeg])``, then the columns
of `V` correspond to the elements of a 3-D coefficient array `c` of
shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

.. math:: c_{000}, c_{001}, c_{002},... , c_{010}, c_{011}, c_{012},...

and  ``np.dot(V, c.flat)`` and ``polyval3d(x, y, z, c)`` will be the
same up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 3-D polynomials
of the same degrees and sample points.

Parameters
----------
x, y, z : array_like
    Arrays of point coordinates, all of the same shape. The dtypes will
    be converted to either float64 or complex128 depending on whether
    any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg, z_deg].

Returns
-------
vander3d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg([1]+1)*(deg[2]+1)`.  The dtype will
    be the same as the converted `x`, `y`, and `z`.

See Also
--------
polyvander, polyvander3d, polyval2d, polyval3d

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial import polynomial as P
>>> x = np.asarray([-1, 2, 1])
>>> y = np.asarray([1, -2, -3])
>>> z = np.asarray([2, 2, 5])
>>> l, m, n = [2, 2, 1]
>>> deg = [l, m, n]
>>> V = P.polyvander3d(x=x, y=y, z=z, deg=deg)
>>> V
array([[  1.,   2.,   1.,   2.,   1.,   2.,  -1.,  -2.,  -1.,
         -2.,  -1.,  -2.,   1.,   2.,   1.,   2.,   1.,   2.],
       [  1.,   2.,  -2.,  -4.,   4.,   8.,   2.,   4.,  -4.,
         -8.,   8.,  16.,   4.,   8.,  -8., -16.,  16.,  32.],
       [  1.,   5.,  -3., -15.,   9.,  45.,   1.,   5.,  -3.,
        -15.,   9.,  45.,   1.,   5.,  -3., -15.,   9.,  45.]])

We can verify the columns for any ``0 <= i <= l``, ``0 <= j <= m``,
and ``0 <= k <= n``

>>> i, j, k = 2, 1, 0
>>> V[:, (m+1)*(n+1)*i + (n+1)*j + k] == x**i * y**j * z**k
array([ True,  True,  True])
- `polyvander2d` (ID: a3dd6401-7b97-487e-a8d3-761a919411da): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y)``. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (deg[1] + 1)*i + j] = x^i * y^j,

where ``0 <= i <= deg[0]`` and ``0 <= j <= deg[1]``. The leading indices of
`V` index the points ``(x, y)`` and the last index encodes the powers of
`x` and `y`.

If ``V = polyvander2d(x, y, [xdeg, ydeg])``, then the columns of `V`
correspond to the elements of a 2-D coefficient array `c` of shape
(xdeg + 1, ydeg + 1) in the order

.. math:: c_{00}, c_{01}, c_{02} ... , c_{10}, c_{11}, c_{12} ...

and ``np.dot(V, c.flat)`` and ``polyval2d(x, y, c)`` will be the same
up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 2-D polynomials
of the same degrees and sample points.

Parameters
----------
x, y : array_like
    Arrays of point coordinates, all of the same shape. The dtypes
    will be converted to either float64 or complex128 depending on
    whether any of the elements are complex. Scalars are converted to
    1-D arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg].

Returns
-------
vander2d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg([1]+1)`.  The dtype will be the same
    as the converted `x` and `y`.

See Also
--------
polyvander, polyvander3d, polyval2d, polyval3d

Examples
--------
>>> import numpy as np

The 2-D pseudo-Vandermonde matrix of degree ``[1, 2]`` and sample
points ``x = [-1, 2]`` and ``y = [1, 3]`` is as follows:

>>> from numpy.polynomial import polynomial as P
>>> x = np.array([-1, 2])
>>> y = np.array([1, 3])
>>> m, n = 1, 2
>>> deg = np.array([m, n])
>>> V = P.polyvander2d(x=x, y=y, deg=deg)
>>> V
array([[ 1.,  1.,  1., -1., -1., -1.],
       [ 1.,  3.,  9.,  2.,  6., 18.]])

We can verify the columns for any ``0 <= i <= m`` and ``0 <= j <= n``:

>>> i, j = 0, 1
>>> V[:, (deg[1]+1)*i + j] == x**i * y**j
array([ True,  True])

The (1D) Vandermonde matrix of sample points ``x`` and degree ``m`` is a
special case of the (2D) pseudo-Vandermonde matrix with ``y`` points all
zero and degree ``[m, 0]``.

>>> P.polyvander2d(x=x, y=0*x, deg=(m, 0)) == P.polyvander(x=x, deg=m)
array([[ True,  True],
       [ True,  True]])
- `polyvander` (ID: c4316089-b5ad-4da5-9af1-42782254b25e): Vandermonde matrix of given degree.

Returns the Vandermonde matrix of degree `deg` and sample points
`x`. The Vandermonde matrix is defined by

.. math:: V[..., i] = x^i,

where ``0 <= i <= deg``. The leading indices of `V` index the elements of
`x` and the last index is the power of `x`.

If `c` is a 1-D array of coefficients of length ``n + 1`` and `V` is the
matrix ``V = polyvander(x, n)``, then ``np.dot(V, c)`` and
``polyval(x, c)`` are the same up to roundoff. This equivalence is
useful both for least squares fitting and for the evaluation of a large
number of polynomials of the same degree and sample points.

Parameters
----------
x : array_like
    Array of points. The dtype is converted to float64 or complex128
    depending on whether any of the elements are complex. If `x` is
    scalar it is converted to a 1-D array.
deg : int
    Degree of the resulting matrix.

Returns
-------
vander : ndarray.
    The Vandermonde matrix. The shape of the returned matrix is
    ``x.shape + (deg + 1,)``, where the last index is the power of `x`.
    The dtype will be the same as the converted `x`.

See Also
--------
polyvander2d, polyvander3d

Examples
--------
The Vandermonde matrix of degree ``deg = 5`` and sample points
``x = [-1, 2, 3]`` contains the element-wise powers of `x`
from 0 to 5 as its columns.

>>> from numpy.polynomial import polynomial as P
>>> x, deg = [-1, 2, 3], 5
>>> P.polyvander(x=x, deg=deg)
array([[  1.,  -1.,   1.,  -1.,   1.,  -1.],
       [  1.,   2.,   4.,   8.,  16.,  32.],
       [  1.,   3.,   9.,  27.,  81., 243.]])
- `polyvalfromroots` (ID: d53bc91c-e2ea-4b2c-987f-c9cb77c43a70): Evaluate a polynomial specified by its roots at points x.

If `r` is of length ``N``, this function returns the value

.. math:: p(x) = \prod_{n=1}^{N} (x - r_n)

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `r`.

If `r` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If `r`
is multidimensional, then the shape of the result depends on the value of
`tensor`. If `tensor` is ``True`` the shape will be r.shape[1:] + x.shape;
that is, each polynomial is evaluated at every value of `x`. If `tensor` is
``False``, the shape will be r.shape[1:]; that is, each polynomial is
evaluated only for the corresponding broadcast value of `x`. Note that
scalars have shape (,).

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    with themselves and with the elements of `r`.
r : array_like
    Array of roots. If `r` is multidimensional the first index is the
    root index, while the remaining indices enumerate multiple
    polynomials. For instance, in the two dimensional case the roots
    of each polynomial may be thought of as stored in the columns of `r`.
tensor : boolean, optional
    If True, the shape of the roots array is extended with ones on the
    right, one for each dimension of `x`. Scalars have dimension 0 for this
    action. The result is that every column of coefficients in `r` is
    evaluated for every element of `x`. If False, `x` is broadcast over the
    columns of `r` for the evaluation.  This keyword is useful when `r` is
    multidimensional. The default value is True.

Returns
-------
values : ndarray, compatible object
    The shape of the returned array is described above.

See Also
--------
polyroots, polyfromroots, polyval

Examples
--------
>>> from numpy.polynomial.polynomial import polyvalfromroots
>>> polyvalfromroots(1, [1, 2, 3])
0.0
>>> a = np.arange(4).reshape(2, 2)
>>> a
array([[0, 1],
       [2, 3]])
>>> polyvalfromroots(a, [-1, 0, 1])
array([[-0.,   0.],
       [ 6.,  24.]])
>>> r = np.arange(-2, 2).reshape(2,2)  # multidimensional coefficients
>>> r # each column of r defines one polynomial
array([[-2, -1],
       [ 0,  1]])
>>> b = [-2, 1]
>>> polyvalfromroots(b, r, tensor=True)
array([[-0.,  3.],
       [ 3., 0.]])
>>> polyvalfromroots(b, r, tensor=False)
array([-0.,  0.])
- `polyval3d` (ID: c3e4d014-d299-419c-863d-fd89c752333c): Evaluate a 3-D polynomial at points (x, y, z).

This function returns the values:

.. math:: p(x,y,z) = \sum_{i,j,k} c_{i,j,k} * x^i * y^j * z^k

The parameters `x`, `y`, and `z` are converted to arrays only if
they are tuples or a lists, otherwise they are treated as a scalars and
they must have the same shape after conversion. In either case, either
`x`, `y`, and `z` or their elements must support multiplication and
addition both with themselves and with the elements of `c`.

If `c` has fewer than 3 dimensions, ones are implicitly appended to its
shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape.

Parameters
----------
x, y, z : array_like, compatible object
    The three dimensional series is evaluated at the points
    ``(x, y, z)``, where `x`, `y`, and `z` must have the same shape.  If
    any of `x`, `y`, or `z` is a list or tuple, it is first converted
    to an ndarray, otherwise it is left unchanged and if it isn't an
    ndarray it is  treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j,k is contained in ``c[i,j,k]``. If `c` has dimension
    greater than 3 the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the multidimensional polynomial on points formed with
    triples of corresponding values from `x`, `y`, and `z`.

See Also
--------
polyval, polyval2d, polygrid2d, polygrid3d

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
>>> P.polyval3d(1, 1, 1, c)
45.0
- `polyval2d` (ID: 6fc9f276-26a1-4d8c-8e18-0b0854a72254): Evaluate a 2-D polynomial at points (x, y).

This function returns the value

.. math:: p(x,y) = \sum_{i,j} c_{i,j} * x^i * y^j

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars and they
must have the same shape after conversion. In either case, either `x`
and `y` or their elements must support multiplication and addition both
with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points ``(x, y)``,
    where `x` and `y` must have the same shape. If `x` or `y` is a list
    or tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term
    of multi-degree i,j is contained in ``c[i,j]``. If `c` has
    dimension greater than two the remaining indices enumerate multiple
    sets of coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points formed with
    pairs of corresponding values from `x` and `y`.

See Also
--------
polyval, polygrid2d, polyval3d, polygrid3d

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = ((1, 2, 3), (4, 5, 6))
>>> P.polyval2d(1, 1, c)
21.0
- `polyval` (ID: af4e271f-ca4c-47c0-9e00-2721e91e288f): Evaluate a polynomial at points x.

If `c` is of length ``n + 1``, this function returns the value

.. math:: p(x) = c_0 + c_1 * x + ... + c_n * x^n

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `c`.

If `c` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If
`c` is multidimensional, then the shape of the result depends on the
value of `tensor`. If `tensor` is true the shape will be c.shape[1:] +
x.shape. If `tensor` is false the shape will be c.shape[1:]. Note that
scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so
they should be avoided if efficiency is a concern.

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    with themselves and with the elements of `c`.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree n are contained in c[n]. If `c` is multidimensional the
    remaining indices enumerate multiple polynomials. In the two
    dimensional case the coefficients may be thought of as stored in
    the columns of `c`.
tensor : boolean, optional
    If True, the shape of the coefficient array is extended with ones
    on the right, one for each dimension of `x`. Scalars have dimension 0
    for this action. The result is that every column of coefficients in
    `c` is evaluated for every element of `x`. If False, `x` is broadcast
    over the columns of `c` for the evaluation.  This keyword is useful
    when `c` is multidimensional. The default value is True.

Returns
-------
values : ndarray, compatible object
    The shape of the returned array is described above.

See Also
--------
polyval2d, polygrid2d, polyval3d, polygrid3d

Notes
-----
The evaluation uses Horner's method.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.polynomial import polyval
>>> polyval(1, [1,2,3])
6.0
>>> a = np.arange(4).reshape(2,2)
>>> a
array([[0, 1],
       [2, 3]])
>>> polyval(a, [1, 2, 3])
array([[ 1.,   6.],
       [17.,  34.]])
>>> coef = np.arange(4).reshape(2, 2)  # multidimensional coefficients
>>> coef
array([[0, 1],
       [2, 3]])
>>> polyval([1, 2], coef, tensor=True)
array([[2.,  4.],
       [4.,  7.]])
>>> polyval([1, 2], coef, tensor=False)
array([2.,  7.])
- `polysub` (ID: e4d1071b-82d6-43ff-b88f-41a3e1ca6e5e): Subtract one polynomial from another.

Returns the difference of two polynomials `c1` - `c2`.  The arguments
are sequences of coefficients from lowest order term to highest, i.e.,
[1,2,3] represents the polynomial ``1 + 2*x + 3*x**2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of polynomial coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of coefficients representing their difference.

See Also
--------
polyadd, polymulx, polymul, polydiv, polypow

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c1 = (1, 2, 3)
>>> c2 = (3, 2, 1)
>>> P.polysub(c1,c2)
array([-2.,  0.,  2.])
>>> P.polysub(c2, c1)  # -P.polysub(c1,c2)
array([ 2.,  0., -2.])
- `polyroots` (ID: f0cab038-52cf-423b-9b20-3842fa41f17f): Compute the roots of a polynomial.

Return the roots (a.k.a. "zeros") of the polynomial

.. math:: p(x) = \sum_i c[i] * x^i.

Parameters
----------
c : 1-D array_like
    1-D array of polynomial coefficients.

Returns
-------
out : ndarray
    Array of the roots of the polynomial. If all the roots are real,
    then `out` is also real, otherwise it is complex.

See Also
--------
numpy.polynomial.chebyshev.chebroots
numpy.polynomial.legendre.legroots
numpy.polynomial.laguerre.lagroots
numpy.polynomial.hermite.hermroots
numpy.polynomial.hermite_e.hermeroots

Notes
-----
The root estimates are obtained as the eigenvalues of the companion
matrix, Roots far from the origin of the complex plane may have large
errors due to the numerical instability of the power series for such
values. Roots with multiplicity greater than 1 will also show larger
errors as the value of the series near such points is relatively
insensitive to errors in the roots. Isolated roots near the origin can
be improved by a few iterations of Newton's method.

Examples
--------
>>> import numpy.polynomial.polynomial as poly
>>> poly.polyroots(poly.polyfromroots((-1,0,1)))
array([-1.,  0.,  1.])
>>> poly.polyroots(poly.polyfromroots((-1,0,1))).dtype
dtype('float64')
>>> j = complex(0,1)
>>> poly.polyroots(poly.polyfromroots((-j,0,j)))
array([  0.00000000e+00+0.j,   0.00000000e+00+1.j,   2.77555756e-17-1.j])  # may vary
- `polypow` (ID: b5a53e9b-f342-404f-a160-d91b01bc9e71): Raise a polynomial to a power.

Returns the polynomial `c` raised to the power `pow`. The argument
`c` is a sequence of coefficients ordered from low to high. i.e.,
[1,2,3] is the series  ``1 + 2*x + 3*x**2.``

Parameters
----------
c : array_like
    1-D array of array of series coefficients ordered from low to
    high degree.
pow : integer
    Power to which the series will be raised
maxpower : integer, optional
    Maximum power allowed. This is mainly to limit growth of the series
    to unmanageable size. Default is 16

Returns
-------
coef : ndarray
    Power series of power.

See Also
--------
polyadd, polysub, polymulx, polymul, polydiv

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> P.polypow([1, 2, 3], 2)
array([ 1., 4., 10., 12., 9.])
- `polymulx` (ID: bbcbf6d2-8c58-4052-8537-fec51adf7521): Multiply a polynomial by x.

Multiply the polynomial `c` by x, where x is the independent
variable.


Parameters
----------
c : array_like
    1-D array of polynomial coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the result of the multiplication.

See Also
--------
polyadd, polysub, polymul, polydiv, polypow

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = (1, 2, 3)
>>> P.polymulx(c)
array([0., 1., 2., 3.])
- `polymul` (ID: f38bc31d-a074-4fa3-a5ca-9885d3a6236d): Multiply one polynomial by another.

Returns the product of two polynomials `c1` * `c2`.  The arguments are
sequences of coefficients, from lowest order term to highest, e.g.,
[1,2,3] represents the polynomial ``1 + 2*x + 3*x**2.``

Parameters
----------
c1, c2 : array_like
    1-D arrays of coefficients representing a polynomial, relative to the
    "standard" basis, and ordered from lowest order term to highest.

Returns
-------
out : ndarray
    Of the coefficients of their product.

See Also
--------
polyadd, polysub, polymulx, polydiv, polypow

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c1 = (1, 2, 3)
>>> c2 = (3, 2, 1)
>>> P.polymul(c1, c2)
array([  3.,   8.,  14.,   8.,   3.])
- `polyline` (ID: 16e5c0c3-4c43-464e-b6ea-c5d2b969c89d): Returns an array representing a linear polynomial.

Parameters
----------
off, scl : scalars
    The "y-intercept" and "slope" of the line, respectively.

Returns
-------
y : ndarray
    This module's representation of the linear polynomial ``off +
    scl*x``.

See Also
--------
numpy.polynomial.chebyshev.chebline
numpy.polynomial.legendre.legline
numpy.polynomial.laguerre.lagline
numpy.polynomial.hermite.hermline
numpy.polynomial.hermite_e.hermeline

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> P.polyline(1, -1)
array([ 1, -1])
>>> P.polyval(1, P.polyline(1, -1))  # should be 0
0.0
- `polyint` (ID: 46848d5f-4deb-4bfe-b197-32ca505841e5): Integrate a polynomial.

Returns the polynomial coefficients `c` integrated `m` times from
`lbnd` along `axis`.  At each iteration the resulting series is
**multiplied** by `scl` and an integration constant, `k`, is added.
The scaling factor is for use in a linear change of variable.  ("Buyer
beware": note that, depending on what one is doing, one may want `scl`
to be the reciprocal of what one might expect; for more information,
see the Notes section below.) The argument `c` is an array of
coefficients, from low to high degree along each axis, e.g., [1,2,3]
represents the polynomial ``1 + 2*x + 3*x**2`` while [[1,2],[1,2]]
represents ``1 + 1*x + 2*y + 2*x*y`` if axis=0 is ``x`` and axis=1 is
``y``.

Parameters
----------
c : array_like
    1-D array of polynomial coefficients, ordered from low to high.
m : int, optional
    Order of integration, must be positive. (Default: 1)
k : {[], list, scalar}, optional
    Integration constant(s).  The value of the first integral at zero
    is the first value in the list, the value of the second integral
    at zero is the second value, etc.  If ``k == []`` (the default),
    all constants are set to zero.  If ``m == 1``, a single scalar can
    be given instead of a list.
lbnd : scalar, optional
    The lower bound of the integral. (Default: 0)
scl : scalar, optional
    Following each integration the result is *multiplied* by `scl`
    before the integration constant is added. (Default: 1)
axis : int, optional
    Axis over which the integral is taken. (Default: 0).

Returns
-------
S : ndarray
    Coefficient array of the integral.

Raises
------
ValueError
    If ``m < 1``, ``len(k) > m``, ``np.ndim(lbnd) != 0``, or
    ``np.ndim(scl) != 0``.

See Also
--------
polyder

Notes
-----
Note that the result of each integration is *multiplied* by `scl`.  Why
is this important to note?  Say one is making a linear change of
variable :math:`u = ax + b` in an integral relative to `x`. Then
:math:`dx = du/a`, so one will need to set `scl` equal to
:math:`1/a` - perhaps not what one would have first thought.

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = (1, 2, 3)
>>> P.polyint(c)  # should return array([0, 1, 1, 1])
array([0.,  1.,  1.,  1.])
>>> P.polyint(c, 3)  # should return array([0, 0, 0, 1/6, 1/12, 1/20])
 array([ 0.        ,  0.        ,  0.        ,  0.16666667,  0.08333333, # may vary
         0.05      ])
>>> P.polyint(c, k=3)  # should return array([3, 1, 1, 1])
array([3.,  1.,  1.,  1.])
>>> P.polyint(c,lbnd=-2)  # should return array([6, 1, 1, 1])
array([6.,  1.,  1.,  1.])
>>> P.polyint(c,scl=-2)  # should return array([0, -2, -2, -2])
array([ 0., -2., -2., -2.])
- `polygrid3d` (ID: 48d8778b-a887-4a5c-b2c3-fbca4156579e): Evaluate a 3-D polynomial on the Cartesian product of x, y and z.

This function returns the values:

.. math:: p(a,b,c) = \sum_{i,j,k} c_{i,j,k} * a^i * b^j * c^k

where the points ``(a, b, c)`` consist of all triples formed by taking
`a` from `x`, `b` from `y`, and `c` from `z`. The resulting points form
a grid with `x` in the first dimension, `y` in the second, and `z` in
the third.

The parameters `x`, `y`, and `z` are converted to arrays only if they
are tuples or a lists, otherwise they are treated as a scalars. In
either case, either `x`, `y`, and `z` or their elements must support
multiplication and addition both with themselves and with the elements
of `c`.

If `c` has fewer than three dimensions, ones are implicitly appended to
its shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape + y.shape + z.shape.

Parameters
----------
x, y, z : array_like, compatible objects
    The three dimensional series is evaluated at the points in the
    Cartesian product of `x`, `y`, and `z`.  If `x`, `y`, or `z` is a
    list or tuple, it is first converted to an ndarray, otherwise it is
    left unchanged and, if it isn't an ndarray, it is treated as a
    scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
polyval, polyval2d, polygrid2d, polyval3d

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
>>> P.polygrid3d([0, 1], [0, 1], [0, 1], c)
array([[ 1., 13.],
       [ 6., 51.]])
- `polygrid2d` (ID: c4174e7c-820b-4411-8c44-31bd98e48cd4): Evaluate a 2-D polynomial on the Cartesian product of x and y.

This function returns the values:

.. math:: p(a,b) = \sum_{i,j} c_{i,j} * a^i * b^j

where the points ``(a, b)`` consist of all pairs formed by taking
`a` from `x` and `b` from `y`. The resulting points form a grid with
`x` in the first dimension and `y` in the second.

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars. In either
case, either `x` and `y` or their elements must support multiplication
and addition both with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape + y.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points in the
    Cartesian product of `x` and `y`.  If `x` or `y` is a list or
    tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
polyval, polyval2d, polyval3d, polygrid3d

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = ((1, 2, 3), (4, 5, 6))
>>> P.polygrid2d([0, 1], [0, 1], c)
array([[ 1.,  6.],
       [ 5., 21.]])
- `polyfromroots` (ID: 7ec6bb9a-bcf0-4344-97c8-8d556875e001): Generate a monic polynomial with given roots.

Return the coefficients of the polynomial

.. math:: p(x) = (x - r_0) * (x - r_1) * ... * (x - r_n),

where the :math:`r_n` are the roots specified in `roots`.  If a zero has
multiplicity n, then it must appear in `roots` n times. For instance,
if 2 is a root of multiplicity three and 3 is a root of multiplicity 2,
then `roots` looks something like [2, 2, 2, 3, 3]. The roots can appear
in any order.

If the returned coefficients are `c`, then

.. math:: p(x) = c_0 + c_1 * x + ... +  x^n

The coefficient of the last term is 1 for monic polynomials in this
form.

Parameters
----------
roots : array_like
    Sequence containing the roots.

Returns
-------
out : ndarray
    1-D array of the polynomial's coefficients If all the roots are
    real, then `out` is also real, otherwise it is complex.  (see
    Examples below).

See Also
--------
numpy.polynomial.chebyshev.chebfromroots
numpy.polynomial.legendre.legfromroots
numpy.polynomial.laguerre.lagfromroots
numpy.polynomial.hermite.hermfromroots
numpy.polynomial.hermite_e.hermefromroots

Notes
-----
The coefficients are determined by multiplying together linear factors
of the form ``(x - r_i)``, i.e.

.. math:: p(x) = (x - r_0) (x - r_1) ... (x - r_n)

where ``n == len(roots) - 1``; note that this implies that ``1`` is always
returned for :math:`a_n`.

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> P.polyfromroots((-1,0,1))  # x(x - 1)(x + 1) = x^3 - x
array([ 0., -1.,  0.,  1.])
>>> j = complex(0,1)
>>> P.polyfromroots((-j,j))  # complex returned, though values are real
array([1.+0.j,  0.+0.j,  1.+0.j])
- `polyfit` (ID: 37078501-b7b9-4e23-a437-ac757e39c713): Least-squares fit of a polynomial to data.

Return the coefficients of a polynomial of degree `deg` that is the
least squares fit to the data values `y` given at points `x`. If `y` is
1-D the returned coefficients will also be 1-D. If `y` is 2-D multiple
fits are done, one for each column of `y`, and the resulting
coefficients are stored in the corresponding columns of a 2-D return.
The fitted polynomial(s) are in the form

.. math::  p(x) = c_0 + c_1 * x + ... + c_n * x^n,

where `n` is `deg`.

Parameters
----------
x : array_like, shape (`M`,)
    x-coordinates of the `M` sample (data) points ``(x[i], y[i])``.
y : array_like, shape (`M`,) or (`M`, `K`)
    y-coordinates of the sample points.  Several sets of sample points
    sharing the same x-coordinates can be (independently) fit with one
    call to `polyfit` by passing in for `y` a 2-D array that contains
    one data set per column.
deg : int or 1-D array_like
    Degree(s) of the fitting polynomials. If `deg` is a single integer
    all terms up to and including the `deg`'th term are included in the
    fit. For NumPy versions >= 1.11.0 a list of integers specifying the
    degrees of the terms to include may be used instead.
rcond : float, optional
    Relative condition number of the fit.  Singular values smaller
    than `rcond`, relative to the largest singular value, will be
    ignored.  The default value is ``len(x)*eps``, where `eps` is the
    relative precision of the platform's float type, about 2e-16 in
    most cases.
full : bool, optional
    Switch determining the nature of the return value.  When ``False``
    (the default) just the coefficients are returned; when ``True``,
    diagnostic information from the singular value decomposition (used
    to solve the fit's matrix equation) is also returned.
w : array_like, shape (`M`,), optional
    Weights. If not None, the weight ``w[i]`` applies to the unsquared
    residual ``y[i] - y_hat[i]`` at ``x[i]``. Ideally the weights are
    chosen so that the errors of the products ``w[i]*y[i]`` all have the
    same variance.  When using inverse-variance weighting, use
    ``w[i] = 1/sigma(y[i])``.  The default value is None.

Returns
-------
coef : ndarray, shape (`deg` + 1,) or (`deg` + 1, `K`)
    Polynomial coefficients ordered from low to high.  If `y` was 2-D,
    the coefficients in column `k` of `coef` represent the polynomial
    fit to the data in `y`'s `k`-th column.

[residuals, rank, singular_values, rcond] : list
    These values are only returned if ``full == True``

    - residuals -- sum of squared residuals of the least squares fit
    - rank -- the numerical rank of the scaled Vandermonde matrix
    - singular_values -- singular values of the scaled Vandermonde matrix
    - rcond -- value of `rcond`.

    For more details, see `numpy.linalg.lstsq`.

Raises
------
RankWarning
    Raised if the matrix in the least-squares fit is rank deficient.
    The warning is only raised if ``full == False``.  The warnings can
    be turned off by:

    >>> import warnings
    >>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

See Also
--------
numpy.polynomial.chebyshev.chebfit
numpy.polynomial.legendre.legfit
numpy.polynomial.laguerre.lagfit
numpy.polynomial.hermite.hermfit
numpy.polynomial.hermite_e.hermefit
polyval : Evaluates a polynomial.
polyvander : Vandermonde matrix for powers.
numpy.linalg.lstsq : Computes a least-squares fit from the matrix.
scipy.interpolate.UnivariateSpline : Computes spline fits.

Notes
-----
The solution is the coefficients of the polynomial `p` that minimizes
the sum of the weighted squared errors

.. math:: E = \sum_j w_j^2 * |y_j - p(x_j)|^2,

where the :math:`w_j` are the weights. This problem is solved by
setting up the (typically) over-determined matrix equation:

.. math:: V(x) * c = w * y,

where `V` is the weighted pseudo Vandermonde matrix of `x`, `c` are the
coefficients to be solved for, `w` are the weights, and `y` are the
observed values.  This equation is then solved using the singular value
decomposition of `V`.

If some of the singular values of `V` are so small that they are
neglected (and `full` == ``False``), a `~exceptions.RankWarning` will be
raised.  This means that the coefficient values may be poorly determined.
Fitting to a lower order polynomial will usually get rid of the warning
(but may not be what you want, of course; if you have independent
reason(s) for choosing the degree which isn't working, you may have to:
a) reconsider those reasons, and/or b) reconsider the quality of your
data).  The `rcond` parameter can also be set to a value smaller than
its default, but the resulting fit may be spurious and have large
contributions from roundoff error.

Polynomial fits using double precision tend to "fail" at about
(polynomial) degree 20. Fits using Chebyshev or Legendre series are
generally better conditioned, but much can still depend on the
distribution of the sample points and the smoothness of the data.  If
the quality of the fit is inadequate, splines may be a good
alternative.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial import polynomial as P
>>> x = np.linspace(-1,1,51)  # x "data": [-1, -0.96, ..., 0.96, 1]
>>> rng = np.random.default_rng()
>>> err = rng.normal(size=len(x))
>>> y = x**3 - x + err  # x^3 - x + Gaussian noise
>>> c, stats = P.polyfit(x,y,3,full=True)
>>> c # c[0], c[1] approx. -1, c[2] should be approx. 0, c[3] approx. 1
array([ 0.23111996, -1.02785049, -0.2241444 ,  1.08405657]) # may vary
>>> stats # note the large SSR, explaining the rather poor results
[array([48.312088]),                                        # may vary
 4,
 array([1.38446749, 1.32119158, 0.50443316, 0.28853036]),
 1.1324274851176597e-14]

Same thing without the added noise

>>> y = x**3 - x
>>> c, stats = P.polyfit(x,y,3,full=True)
>>> c # c[0], c[1] ~= -1, c[2] should be "very close to 0", c[3] ~= 1
array([-6.73496154e-17, -1.00000000e+00,  0.00000000e+00,  1.00000000e+00])
>>> stats # note the minuscule SSR
[array([8.79579319e-31]),
 np.int32(4),
 array([1.38446749, 1.32119158, 0.50443316, 0.28853036]),
 1.1324274851176597e-14]
- `polydiv` (ID: ed0f2657-9973-40de-be8f-3d8be581fc2b): Divide one polynomial by another.

Returns the quotient-with-remainder of two polynomials `c1` / `c2`.
The arguments are sequences of coefficients, from lowest order term
to highest, e.g., [1,2,3] represents ``1 + 2*x + 3*x**2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of polynomial coefficients ordered from low to high.

Returns
-------
[quo, rem] : ndarrays
    Of coefficient series representing the quotient and remainder.

See Also
--------
polyadd, polysub, polymulx, polymul, polypow

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c1 = (1, 2, 3)
>>> c2 = (3, 2, 1)
>>> P.polydiv(c1, c2)
(array([3.]), array([-8., -4.]))
>>> P.polydiv(c2, c1)
(array([ 0.33333333]), array([ 2.66666667,  1.33333333]))  # may vary
- `polyder` (ID: b72bc8d1-702f-4216-a315-8640de19126d): Differentiate a polynomial.

Returns the polynomial coefficients `c` differentiated `m` times along
`axis`.  At each iteration the result is multiplied by `scl` (the
scaling factor is for use in a linear change of variable).  The
argument `c` is an array of coefficients from low to high degree along
each axis, e.g., [1,2,3] represents the polynomial ``1 + 2*x + 3*x**2``
while [[1,2],[1,2]] represents ``1 + 1*x + 2*y + 2*x*y`` if axis=0 is
``x`` and axis=1 is ``y``.

Parameters
----------
c : array_like
    Array of polynomial coefficients. If c is multidimensional the
    different axis correspond to different variables with the degree
    in each axis given by the corresponding index.
m : int, optional
    Number of derivatives taken, must be non-negative. (Default: 1)
scl : scalar, optional
    Each differentiation is multiplied by `scl`.  The end result is
    multiplication by ``scl**m``.  This is for use in a linear change
    of variable. (Default: 1)
axis : int, optional
    Axis over which the derivative is taken. (Default: 0).

Returns
-------
der : ndarray
    Polynomial coefficients of the derivative.

See Also
--------
polyint

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = (1, 2, 3, 4)
>>> P.polyder(c)  # (d/dx)(c)
array([  2.,   6.,  12.])
>>> P.polyder(c, 3)  # (d**3/dx**3)(c)
array([24.])
>>> P.polyder(c, scl=-1)  # (d/d(-x))(c)
array([ -2.,  -6., -12.])
>>> P.polyder(c, 2, -1)  # (d**2/d(-x)**2)(c)
array([  6.,  24.])
- `polycompanion` (ID: b3f8ac64-c9e5-498c-85da-7f0b992a1193): Return the companion matrix of c.

The companion matrix for power series cannot be made symmetric by
scaling the basis, so this function differs from those for the
orthogonal polynomials.

Parameters
----------
c : array_like
    1-D array of polynomial coefficients ordered from low to high
    degree.

Returns
-------
mat : ndarray
    Companion matrix of dimensions (deg, deg).

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c = (1, 2, 3)
>>> P.polycompanion(c)
array([[ 0.        , -0.33333333],
       [ 1.        , -0.66666667]])
- `polyadd` (ID: 10c8531a-8714-4d50-b465-f4e11f753b0c): Add one polynomial to another.

Returns the sum of two polynomials `c1` + `c2`.  The arguments are
sequences of coefficients from lowest order term to highest, i.e.,
[1,2,3] represents the polynomial ``1 + 2*x + 3*x**2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of polynomial coefficients ordered from low to high.

Returns
-------
out : ndarray
    The coefficient array representing their sum.

See Also
--------
polysub, polymulx, polymul, polydiv, polypow

Examples
--------
>>> from numpy.polynomial import polynomial as P
>>> c1 = (1, 2, 3)
>>> c2 = (3, 2, 1)
>>> sum = P.polyadd(c1,c2); sum
array([4.,  4.,  4.])
>>> P.polyval(2, sum)  # 4 + 4(2) + 4(2**2)
28.0
- `poly2leg` (ID: 62dcc364-2183-425b-b402-46dd08896931): Convert a polynomial to a Legendre series.

Convert an array representing the coefficients of a polynomial (relative
to the "standard" basis) ordered from lowest degree to highest, to an
array of the coefficients of the equivalent Legendre series, ordered
from lowest to highest degree.

Parameters
----------
pol : array_like
    1-D array containing the polynomial coefficients

Returns
-------
c : ndarray
    1-D array containing the coefficients of the equivalent Legendre
    series.

See Also
--------
leg2poly

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> import numpy as np
>>> from numpy import polynomial as P
>>> p = P.Polynomial(np.arange(4))
>>> p
Polynomial([0.,  1.,  2.,  3.], domain=[-1.,  1.], window=[-1.,  1.], ...
>>> c = P.Legendre(P.legendre.poly2leg(p.coef))
>>> c
Legendre([ 1.  ,  3.25,  1.  ,  0.75], domain=[-1,  1], window=[-1,  1]) # may vary
- `legweight` (ID: ecae5e43-b743-426b-b1b1-9fe4b75aacdf): Weight function of the Legendre polynomials.

The weight function is :math:`1` and the interval of integration is
:math:`[-1, 1]`. The Legendre polynomials are orthogonal, but not
normalized, with respect to this weight function.

Parameters
----------
x : array_like
   Values at which the weight function will be computed.

Returns
-------
w : ndarray
   The weight function at `x`.
- `legvander3d` (ID: 7442cf22-a2ae-4a8e-9e91-aee5abfff0ae): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y, z)``. If `l`, `m`, `n` are the given degrees in `x`, `y`, `z`,
then The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (m+1)(n+1)i + (n+1)j + k] = L_i(x)*L_j(y)*L_k(z),

where ``0 <= i <= l``, ``0 <= j <= m``, and ``0 <= j <= n``.  The leading
indices of `V` index the points ``(x, y, z)`` and the last index encodes
the degrees of the Legendre polynomials.

If ``V = legvander3d(x, y, z, [xdeg, ydeg, zdeg])``, then the columns
of `V` correspond to the elements of a 3-D coefficient array `c` of
shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

.. math:: c_{000}, c_{001}, c_{002},... , c_{010}, c_{011}, c_{012},...

and ``np.dot(V, c.flat)`` and ``legval3d(x, y, z, c)`` will be the
same up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 3-D Legendre
series of the same degrees and sample points.

Parameters
----------
x, y, z : array_like
    Arrays of point coordinates, all of the same shape. The dtypes will
    be converted to either float64 or complex128 depending on whether
    any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg, z_deg].

Returns
-------
vander3d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)*(deg[2]+1)`.  The dtype will
    be the same as the converted `x`, `y`, and `z`.

See Also
--------
legvander, legvander3d, legval2d, legval3d
- `legvander2d` (ID: 535e1635-438a-4f79-bc49-6b9d254d9ffc): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y)``. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (deg[1] + 1)*i + j] = L_i(x) * L_j(y),

where ``0 <= i <= deg[0]`` and ``0 <= j <= deg[1]``. The leading indices of
`V` index the points ``(x, y)`` and the last index encodes the degrees of
the Legendre polynomials.

If ``V = legvander2d(x, y, [xdeg, ydeg])``, then the columns of `V`
correspond to the elements of a 2-D coefficient array `c` of shape
(xdeg + 1, ydeg + 1) in the order

.. math:: c_{00}, c_{01}, c_{02} ... , c_{10}, c_{11}, c_{12} ...

and ``np.dot(V, c.flat)`` and ``legval2d(x, y, c)`` will be the same
up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 2-D Legendre
series of the same degrees and sample points.

Parameters
----------
x, y : array_like
    Arrays of point coordinates, all of the same shape. The dtypes
    will be converted to either float64 or complex128 depending on
    whether any of the elements are complex. Scalars are converted to
    1-D arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg].

Returns
-------
vander2d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)`.  The dtype will be the same
    as the converted `x` and `y`.

See Also
--------
legvander, legvander3d, legval2d, legval3d
- `legvander` (ID: 4ce4be41-3b31-4347-8223-e685a5e06880): Pseudo-Vandermonde matrix of given degree.

Returns the pseudo-Vandermonde matrix of degree `deg` and sample points
`x`. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., i] = L_i(x)

where ``0 <= i <= deg``. The leading indices of `V` index the elements of
`x` and the last index is the degree of the Legendre polynomial.

If `c` is a 1-D array of coefficients of length ``n + 1`` and `V` is the
array ``V = legvander(x, n)``, then ``np.dot(V, c)`` and
``legval(x, c)`` are the same up to roundoff. This equivalence is
useful both for least squares fitting and for the evaluation of a large
number of Legendre series of the same degree and sample points.

Parameters
----------
x : array_like
    Array of points. The dtype is converted to float64 or complex128
    depending on whether any of the elements are complex. If `x` is
    scalar it is converted to a 1-D array.
deg : int
    Degree of the resulting matrix.

Returns
-------
vander : ndarray
    The pseudo-Vandermonde matrix. The shape of the returned matrix is
    ``x.shape + (deg + 1,)``, where The last index is the degree of the
    corresponding Legendre polynomial.  The dtype will be the same as
    the converted `x`.
- `legval3d` (ID: c7768ed7-2a19-48ff-90f9-4d8eb2b05121): Evaluate a 3-D Legendre series at points (x, y, z).

This function returns the values:

.. math:: p(x,y,z) = \sum_{i,j,k} c_{i,j,k} * L_i(x) * L_j(y) * L_k(z)

The parameters `x`, `y`, and `z` are converted to arrays only if
they are tuples or a lists, otherwise they are treated as a scalars and
they must have the same shape after conversion. In either case, either
`x`, `y`, and `z` or their elements must support multiplication and
addition both with themselves and with the elements of `c`.

If `c` has fewer than 3 dimensions, ones are implicitly appended to its
shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape.

Parameters
----------
x, y, z : array_like, compatible object
    The three dimensional series is evaluated at the points
    ``(x, y, z)``, where `x`, `y`, and `z` must have the same shape.  If
    any of `x`, `y`, or `z` is a list or tuple, it is first converted
    to an ndarray, otherwise it is left unchanged and if it isn't an
    ndarray it is  treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j,k is contained in ``c[i,j,k]``. If `c` has dimension
    greater than 3 the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the multidimensional polynomial on points formed with
    triples of corresponding values from `x`, `y`, and `z`.

See Also
--------
legval, legval2d, leggrid2d, leggrid3d
- `legval2d` (ID: fe8ae2a6-9bd5-49ff-bb15-ab3d114dd6ed): Evaluate a 2-D Legendre series at points (x, y).

This function returns the values:

.. math:: p(x,y) = \sum_{i,j} c_{i,j} * L_i(x) * L_j(y)

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars and they
must have the same shape after conversion. In either case, either `x`
and `y` or their elements must support multiplication and addition both
with themselves and with the elements of `c`.

If `c` is a 1-D array a one is implicitly appended to its shape to make
it 2-D. The shape of the result will be c.shape[2:] + x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points ``(x, y)``,
    where `x` and `y` must have the same shape. If `x` or `y` is a list
    or tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and if it isn't an ndarray it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term
    of multi-degree i,j is contained in ``c[i,j]``. If `c` has
    dimension greater than two the remaining indices enumerate multiple
    sets of coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional Legendre series at points formed
    from pairs of corresponding values from `x` and `y`.

See Also
--------
legval, leggrid2d, legval3d, leggrid3d
- `legval` (ID: 65c31e11-dfbe-4024-8565-cb33b801a733): Evaluate a Legendre series at points x.

If `c` is of length ``n + 1``, this function returns the value:

.. math:: p(x) = c_0 * L_0(x) + c_1 * L_1(x) + ... + c_n * L_n(x)

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `c`.

If `c` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If
`c` is multidimensional, then the shape of the result depends on the
value of `tensor`. If `tensor` is true the shape will be c.shape[1:] +
x.shape. If `tensor` is false the shape will be c.shape[1:]. Note that
scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so
they should be avoided if efficiency is a concern.

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    themselves and with the elements of `c`.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree n are contained in c[n]. If `c` is multidimensional the
    remaining indices enumerate multiple polynomials. In the two
    dimensional case the coefficients may be thought of as stored in
    the columns of `c`.
tensor : boolean, optional
    If True, the shape of the coefficient array is extended with ones
    on the right, one for each dimension of `x`. Scalars have dimension 0
    for this action. The result is that every column of coefficients in
    `c` is evaluated for every element of `x`. If False, `x` is broadcast
    over the columns of `c` for the evaluation.  This keyword is useful
    when `c` is multidimensional. The default value is True.

Returns
-------
values : ndarray, algebra_like
    The shape of the return value is described above.

See Also
--------
legval2d, leggrid2d, legval3d, leggrid3d

Notes
-----
The evaluation uses Clenshaw recursion, aka synthetic division.
- `legsub` (ID: 1d836fad-2ff5-437c-b145-d3bacafeb634): Subtract one Legendre series from another.

Returns the difference of two Legendre series `c1` - `c2`.  The
sequences of coefficients are from lowest order term to highest, i.e.,
[1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Legendre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Legendre series coefficients representing their difference.

See Also
--------
legadd, legmulx, legmul, legdiv, legpow

Notes
-----
Unlike multiplication, division, etc., the difference of two Legendre
series is a Legendre series (without having to "reproject" the result
onto the basis set) so subtraction, just like that of "standard"
polynomials, is simply "component-wise."

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> L.legsub(c1,c2)
array([-2.,  0.,  2.])
>>> L.legsub(c2,c1) # -C.legsub(c1,c2)
array([ 2.,  0., -2.])
- `legroots` (ID: efc8620b-5ff5-403e-8f35-928c8fd8b427): Compute the roots of a Legendre series.

Return the roots (a.k.a. "zeros") of the polynomial

.. math:: p(x) = \sum_i c[i] * L_i(x).

Parameters
----------
c : 1-D array_like
    1-D array of coefficients.

Returns
-------
out : ndarray
    Array of the roots of the series. If all the roots are real,
    then `out` is also real, otherwise it is complex.

See Also
--------
numpy.polynomial.polynomial.polyroots
numpy.polynomial.chebyshev.chebroots
numpy.polynomial.laguerre.lagroots
numpy.polynomial.hermite.hermroots
numpy.polynomial.hermite_e.hermeroots

Notes
-----
The root estimates are obtained as the eigenvalues of the companion
matrix, Roots far from the origin of the complex plane may have large
errors due to the numerical instability of the series for such values.
Roots with multiplicity greater than 1 will also show larger errors as
the value of the series near such points is relatively insensitive to
errors in the roots. Isolated roots near the origin can be improved by
a few iterations of Newton's method.

The Legendre series basis polynomials aren't powers of ``x`` so the
results of this function may seem unintuitive.

Examples
--------
>>> import numpy.polynomial.legendre as leg
>>> leg.legroots((1, 2, 3, 4)) # 4L_3 + 3L_2 + 2L_1 + 1L_0, all real roots
array([-0.85099543, -0.11407192,  0.51506735]) # may vary
- `legpow` (ID: a277e3f8-20fd-48d6-83ed-e2ca8b4bc519): Raise a Legendre series to a power.

Returns the Legendre series `c` raised to the power `pow`. The
argument `c` is a sequence of coefficients ordered from low to high.
i.e., [1,2,3] is the series  ``P_0 + 2*P_1 + 3*P_2.``

Parameters
----------
c : array_like
    1-D array of Legendre series coefficients ordered from low to
    high.
pow : integer
    Power to which the series will be raised
maxpower : integer, optional
    Maximum power allowed. This is mainly to limit growth of the series
    to unmanageable size. Default is 16

Returns
-------
coef : ndarray
    Legendre series of power.

See Also
--------
legadd, legsub, legmulx, legmul, legdiv
- `legmulx` (ID: 888f8129-33bf-4809-bd0a-e6fbdfc4ae87): Multiply a Legendre series by x.

Multiply the Legendre series `c` by x, where x is the independent
variable.


Parameters
----------
c : array_like
    1-D array of Legendre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the result of the multiplication.

See Also
--------
legadd, legsub, legmul, legdiv, legpow

Notes
-----
The multiplication uses the recursion relationship for Legendre
polynomials in the form

.. math::

  xP_i(x) = ((i + 1)*P_{i + 1}(x) + i*P_{i - 1}(x))/(2i + 1)

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> L.legmulx([1,2,3])
array([ 0.66666667, 2.2, 1.33333333, 1.8]) # may vary
- `legmul` (ID: c9de71be-86df-4282-8ad6-7e52ea0e1deb): Multiply one Legendre series by another.

Returns the product of two Legendre series `c1` * `c2`.  The arguments
are sequences of coefficients, from lowest order "term" to highest,
e.g., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Legendre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Legendre series coefficients representing their product.

See Also
--------
legadd, legsub, legmulx, legdiv, legpow

Notes
-----
In general, the (polynomial) product of two C-series results in terms
that are not in the Legendre polynomial basis set.  Thus, to express
the product as a Legendre series, it is necessary to "reproject" the
product onto said basis set, which may produce "unintuitive" (but
correct) results; see Examples section below.

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> c1 = (1,2,3)
>>> c2 = (3,2)
>>> L.legmul(c1,c2) # multiplication requires "reprojection"
array([  4.33333333,  10.4       ,  11.66666667,   3.6       ]) # may vary
- `legline` (ID: efb331b5-76db-4334-bf0e-397d815dedec): Legendre series whose graph is a straight line.



Parameters
----------
off, scl : scalars
    The specified line is given by ``off + scl*x``.

Returns
-------
y : ndarray
    This module's representation of the Legendre series for
    ``off + scl*x``.

See Also
--------
numpy.polynomial.polynomial.polyline
numpy.polynomial.chebyshev.chebline
numpy.polynomial.laguerre.lagline
numpy.polynomial.hermite.hermline
numpy.polynomial.hermite_e.hermeline

Examples
--------
>>> import numpy.polynomial.legendre as L
>>> L.legline(3,2)
array([3, 2])
>>> L.legval(-3, L.legline(3,2)) # should be -3
-3.0
- `legint` (ID: 99e34d37-e819-40a5-b9e9-ad40f039d3c6): Integrate a Legendre series.

Returns the Legendre series coefficients `c` integrated `m` times from
`lbnd` along `axis`. At each iteration the resulting series is
**multiplied** by `scl` and an integration constant, `k`, is added.
The scaling factor is for use in a linear change of variable.  ("Buyer
beware": note that, depending on what one is doing, one may want `scl`
to be the reciprocal of what one might expect; for more information,
see the Notes section below.)  The argument `c` is an array of
coefficients from low to high degree along each axis, e.g., [1,2,3]
represents the series ``L_0 + 2*L_1 + 3*L_2`` while [[1,2],[1,2]]
represents ``1*L_0(x)*L_0(y) + 1*L_1(x)*L_0(y) + 2*L_0(x)*L_1(y) +
2*L_1(x)*L_1(y)`` if axis=0 is ``x`` and axis=1 is ``y``.

Parameters
----------
c : array_like
    Array of Legendre series coefficients. If c is multidimensional the
    different axis correspond to different variables with the degree in
    each axis given by the corresponding index.
m : int, optional
    Order of integration, must be positive. (Default: 1)
k : {[], list, scalar}, optional
    Integration constant(s).  The value of the first integral at
    ``lbnd`` is the first value in the list, the value of the second
    integral at ``lbnd`` is the second value, etc.  If ``k == []`` (the
    default), all constants are set to zero.  If ``m == 1``, a single
    scalar can be given instead of a list.
lbnd : scalar, optional
    The lower bound of the integral. (Default: 0)
scl : scalar, optional
    Following each integration the result is *multiplied* by `scl`
    before the integration constant is added. (Default: 1)
axis : int, optional
    Axis over which the integral is taken. (Default: 0).

Returns
-------
S : ndarray
    Legendre series coefficient array of the integral.

Raises
------
ValueError
    If ``m < 0``, ``len(k) > m``, ``np.ndim(lbnd) != 0``, or
    ``np.ndim(scl) != 0``.

See Also
--------
legder

Notes
-----
Note that the result of each integration is *multiplied* by `scl`.
Why is this important to note?  Say one is making a linear change of
variable :math:`u = ax + b` in an integral relative to `x`.  Then
:math:`dx = du/a`, so one will need to set `scl` equal to
:math:`1/a` - perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs
to be "reprojected" onto the C-series basis set.  Thus, typically,
the result of this function is "unintuitive," albeit correct; see
Examples section below.

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> c = (1,2,3)
>>> L.legint(c)
array([ 0.33333333,  0.4       ,  0.66666667,  0.6       ]) # may vary
>>> L.legint(c, 3)
array([  1.66666667e-02,  -1.78571429e-02,   4.76190476e-02, # may vary
         -1.73472348e-18,   1.90476190e-02,   9.52380952e-03])
>>> L.legint(c, k=3)
 array([ 3.33333333,  0.4       ,  0.66666667,  0.6       ]) # may vary
>>> L.legint(c, lbnd=-2)
array([ 7.33333333,  0.4       ,  0.66666667,  0.6       ]) # may vary
>>> L.legint(c, scl=2)
array([ 0.66666667,  0.8       ,  1.33333333,  1.2       ]) # may vary
- `leggrid3d` (ID: 827d472f-7ff1-4316-8713-0bac17f1d497): Evaluate a 3-D Legendre series on the Cartesian product of x, y, and z.

This function returns the values:

.. math:: p(a,b,c) = \sum_{i,j,k} c_{i,j,k} * L_i(a) * L_j(b) * L_k(c)

where the points ``(a, b, c)`` consist of all triples formed by taking
`a` from `x`, `b` from `y`, and `c` from `z`. The resulting points form
a grid with `x` in the first dimension, `y` in the second, and `z` in
the third.

The parameters `x`, `y`, and `z` are converted to arrays only if they
are tuples or a lists, otherwise they are treated as a scalars. In
either case, either `x`, `y`, and `z` or their elements must support
multiplication and addition both with themselves and with the elements
of `c`.

If `c` has fewer than three dimensions, ones are implicitly appended to
its shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape + y.shape + z.shape.

Parameters
----------
x, y, z : array_like, compatible objects
    The three dimensional series is evaluated at the points in the
    Cartesian product of `x`, `y`, and `z`.  If `x`, `y`, or `z` is a
    list or tuple, it is first converted to an ndarray, otherwise it is
    left unchanged and, if it isn't an ndarray, it is treated as a
    scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
legval, legval2d, leggrid2d, legval3d
- `leggrid2d` (ID: f67956c9-8859-4c2b-9975-881e7ce68315): Evaluate a 2-D Legendre series on the Cartesian product of x and y.

This function returns the values:

.. math:: p(a,b) = \sum_{i,j} c_{i,j} * L_i(a) * L_j(b)

where the points ``(a, b)`` consist of all pairs formed by taking
`a` from `x` and `b` from `y`. The resulting points form a grid with
`x` in the first dimension and `y` in the second.

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars. In either
case, either `x` and `y` or their elements must support multiplication
and addition both with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape + y.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points in the
    Cartesian product of `x` and `y`.  If `x` or `y` is a list or
    tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j is contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional Chebyshev series at points in the
    Cartesian product of `x` and `y`.

See Also
--------
legval, legval2d, legval3d, leggrid3d
- `leggauss` (ID: c6687ac6-3a59-46ed-9300-716f3bb7efe2): Gauss-Legendre quadrature.

Computes the sample points and weights for Gauss-Legendre quadrature.
These sample points and weights will correctly integrate polynomials of
degree :math:`2*deg - 1` or less over the interval :math:`[-1, 1]` with
the weight function :math:`f(x) = 1`.

Parameters
----------
deg : int
    Number of sample points and weights. It must be >= 1.

Returns
-------
x : ndarray
    1-D ndarray containing the sample points.
y : ndarray
    1-D ndarray containing the weights.

Notes
-----
The results have only been tested up to degree 100, higher degrees may
be problematic. The weights are determined by using the fact that

.. math:: w_k = c / (L'_n(x_k) * L_{n-1}(x_k))

where :math:`c` is a constant independent of :math:`k` and :math:`x_k`
is the k'th root of :math:`L_n`, and then scaling the results to get
the right value when integrating 1.
- `legfromroots` (ID: 4de60df2-4a44-4d98-aa32-5ee79c287c78): Generate a Legendre series with given roots.

The function returns the coefficients of the polynomial

.. math:: p(x) = (x - r_0) * (x - r_1) * ... * (x - r_n),

in Legendre form, where the :math:`r_n` are the roots specified in `roots`.
If a zero has multiplicity n, then it must appear in `roots` n times.
For instance, if 2 is a root of multiplicity three and 3 is a root of
multiplicity 2, then `roots` looks something like [2, 2, 2, 3, 3]. The
roots can appear in any order.

If the returned coefficients are `c`, then

.. math:: p(x) = c_0 + c_1 * L_1(x) + ... +  c_n * L_n(x)

The coefficient of the last term is not generally 1 for monic
polynomials in Legendre form.

Parameters
----------
roots : array_like
    Sequence containing the roots.

Returns
-------
out : ndarray
    1-D array of coefficients.  If all roots are real then `out` is a
    real array, if some of the roots are complex, then `out` is complex
    even if all the coefficients in the result are real (see Examples
    below).

See Also
--------
numpy.polynomial.polynomial.polyfromroots
numpy.polynomial.chebyshev.chebfromroots
numpy.polynomial.laguerre.lagfromroots
numpy.polynomial.hermite.hermfromroots
numpy.polynomial.hermite_e.hermefromroots

Examples
--------
>>> import numpy.polynomial.legendre as L
>>> L.legfromroots((-1,0,1)) # x^3 - x relative to the standard basis
array([ 0. , -0.4,  0. ,  0.4])
>>> j = complex(0,1)
>>> L.legfromroots((-j,j)) # x^2 + 1 relative to the standard basis
array([ 1.33333333+0.j,  0.00000000+0.j,  0.66666667+0.j]) # may vary
- `legfit` (ID: 5a0d233b-016b-49e2-bfad-8333d0dbc6a7): Least squares fit of Legendre series to data.

Return the coefficients of a Legendre series of degree `deg` that is the
least squares fit to the data values `y` given at points `x`. If `y` is
1-D the returned coefficients will also be 1-D. If `y` is 2-D multiple
fits are done, one for each column of `y`, and the resulting
coefficients are stored in the corresponding columns of a 2-D return.
The fitted polynomial(s) are in the form

.. math::  p(x) = c_0 + c_1 * L_1(x) + ... + c_n * L_n(x),

where `n` is `deg`.

Parameters
----------
x : array_like, shape (M,)
    x-coordinates of the M sample points ``(x[i], y[i])``.
y : array_like, shape (M,) or (M, K)
    y-coordinates of the sample points. Several data sets of sample
    points sharing the same x-coordinates can be fitted at once by
    passing in a 2D-array that contains one dataset per column.
deg : int or 1-D array_like
    Degree(s) of the fitting polynomials. If `deg` is a single integer
    all terms up to and including the `deg`'th term are included in the
    fit. For NumPy versions >= 1.11.0 a list of integers specifying the
    degrees of the terms to include may be used instead.
rcond : float, optional
    Relative condition number of the fit. Singular values smaller than
    this relative to the largest singular value will be ignored. The
    default value is len(x)*eps, where eps is the relative precision of
    the float type, about 2e-16 in most cases.
full : bool, optional
    Switch determining nature of return value. When it is False (the
    default) just the coefficients are returned, when True diagnostic
    information from the singular value decomposition is also returned.
w : array_like, shape (`M`,), optional
    Weights. If not None, the weight ``w[i]`` applies to the unsquared
    residual ``y[i] - y_hat[i]`` at ``x[i]``. Ideally the weights are
    chosen so that the errors of the products ``w[i]*y[i]`` all have the
    same variance.  When using inverse-variance weighting, use
    ``w[i] = 1/sigma(y[i])``.  The default value is None.

Returns
-------
coef : ndarray, shape (M,) or (M, K)
    Legendre coefficients ordered from low to high. If `y` was
    2-D, the coefficients for the data in column k of `y` are in
    column `k`. If `deg` is specified as a list, coefficients for
    terms not included in the fit are set equal to zero in the
    returned `coef`.

[residuals, rank, singular_values, rcond] : list
    These values are only returned if ``full == True``

    - residuals -- sum of squared residuals of the least squares fit
    - rank -- the numerical rank of the scaled Vandermonde matrix
    - singular_values -- singular values of the scaled Vandermonde matrix
    - rcond -- value of `rcond`.

    For more details, see `numpy.linalg.lstsq`.

Warns
-----
RankWarning
    The rank of the coefficient matrix in the least-squares fit is
    deficient. The warning is only raised if ``full == False``.  The
    warnings can be turned off by

    >>> import warnings
    >>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

See Also
--------
numpy.polynomial.polynomial.polyfit
numpy.polynomial.chebyshev.chebfit
numpy.polynomial.laguerre.lagfit
numpy.polynomial.hermite.hermfit
numpy.polynomial.hermite_e.hermefit
legval : Evaluates a Legendre series.
legvander : Vandermonde matrix of Legendre series.
legweight : Legendre weight function (= 1).
numpy.linalg.lstsq : Computes a least-squares fit from the matrix.
scipy.interpolate.UnivariateSpline : Computes spline fits.

Notes
-----
The solution is the coefficients of the Legendre series `p` that
minimizes the sum of the weighted squared errors

.. math:: E = \sum_j w_j^2 * |y_j - p(x_j)|^2,

where :math:`w_j` are the weights. This problem is solved by setting up
as the (typically) overdetermined matrix equation

.. math:: V(x) * c = w * y,

where `V` is the weighted pseudo Vandermonde matrix of `x`, `c` are the
coefficients to be solved for, `w` are the weights, and `y` are the
observed values.  This equation is then solved using the singular value
decomposition of `V`.

If some of the singular values of `V` are so small that they are
neglected, then a `~exceptions.RankWarning` will be issued. This means that
the coefficient values may be poorly determined. Using a lower order fit
will usually get rid of the warning.  The `rcond` parameter can also be
set to a value smaller than its default, but the resulting fit may be
spurious and have large contributions from roundoff error.

Fits using Legendre series are usually better conditioned than fits
using power series, but much can depend on the distribution of the
sample points and the smoothness of the data. If the quality of the fit
is inadequate splines may be a good alternative.

References
----------
.. [1] Wikipedia, "Curve fitting",
       https://en.wikipedia.org/wiki/Curve_fitting

Examples
--------
- `legdiv` (ID: 7b2258de-9736-4e32-843c-9223b3986b0f): Divide one Legendre series by another.

Returns the quotient-with-remainder of two Legendre series
`c1` / `c2`.  The arguments are sequences of coefficients from lowest
order "term" to highest, e.g., [1,2,3] represents the series
``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Legendre series coefficients ordered from low to
    high.

Returns
-------
quo, rem : ndarrays
    Of Legendre series coefficients representing the quotient and
    remainder.

See Also
--------
legadd, legsub, legmulx, legmul, legpow

Notes
-----
In general, the (polynomial) division of one Legendre series by another
results in quotient and remainder terms that are not in the Legendre
polynomial basis set.  Thus, to express these results as a Legendre
series, it is necessary to "reproject" the results onto the Legendre
basis set, which may produce "unintuitive" (but correct) results; see
Examples section below.

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> L.legdiv(c1,c2) # quotient "intuitive," remainder not
(array([3.]), array([-8., -4.]))
>>> c2 = (0,1,2,3)
>>> L.legdiv(c2,c1) # neither "intuitive"
(array([-0.07407407,  1.66666667]), array([-1.03703704, -2.51851852])) # may vary
- `legder` (ID: 58ba4272-23e3-4c4b-b54f-454541beb16a): Differentiate a Legendre series.

Returns the Legendre series coefficients `c` differentiated `m` times
along `axis`.  At each iteration the result is multiplied by `scl` (the
scaling factor is for use in a linear change of variable). The argument
`c` is an array of coefficients from low to high degree along each
axis, e.g., [1,2,3] represents the series ``1*L_0 + 2*L_1 + 3*L_2``
while [[1,2],[1,2]] represents ``1*L_0(x)*L_0(y) + 1*L_1(x)*L_0(y) +
2*L_0(x)*L_1(y) + 2*L_1(x)*L_1(y)`` if axis=0 is ``x`` and axis=1 is
``y``.

Parameters
----------
c : array_like
    Array of Legendre series coefficients. If c is multidimensional the
    different axis correspond to different variables with the degree in
    each axis given by the corresponding index.
m : int, optional
    Number of derivatives taken, must be non-negative. (Default: 1)
scl : scalar, optional
    Each differentiation is multiplied by `scl`.  The end result is
    multiplication by ``scl**m``.  This is for use in a linear change of
    variable. (Default: 1)
axis : int, optional
    Axis over which the derivative is taken. (Default: 0).

Returns
-------
der : ndarray
    Legendre series of the derivative.

See Also
--------
legint

Notes
-----
In general, the result of differentiating a Legendre series does not
resemble the same operation on a power series. Thus the result of this
function may be "unintuitive," albeit correct; see Examples section
below.

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> c = (1,2,3,4)
>>> L.legder(c)
array([  6.,   9.,  20.])
>>> L.legder(c, 3)
array([60.])
>>> L.legder(c, scl=-1)
array([ -6.,  -9., -20.])
>>> L.legder(c, 2,-1)
array([  9.,  60.])
- `legcompanion` (ID: 0312a372-35bb-4026-952a-8408dd86e8cd): Return the scaled companion matrix of c.

The basis polynomials are scaled so that the companion matrix is
symmetric when `c` is an Legendre basis polynomial. This provides
better eigenvalue estimates than the unscaled case and for basis
polynomials the eigenvalues are guaranteed to be real if
`numpy.linalg.eigvalsh` is used to obtain them.

Parameters
----------
c : array_like
    1-D array of Legendre series coefficients ordered from low to high
    degree.

Returns
-------
mat : ndarray
    Scaled companion matrix of dimensions (deg, deg).
- `legadd` (ID: 3844d489-ae9d-4655-8ba8-e67379daa740): Add one Legendre series to another.

Returns the sum of two Legendre series `c1` + `c2`.  The arguments
are sequences of coefficients ordered from lowest order term to
highest, i.e., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Legendre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the Legendre series of their sum.

See Also
--------
legsub, legmulx, legmul, legdiv, legpow

Notes
-----
Unlike multiplication, division, etc., the sum of two Legendre series
is a Legendre series (without having to "reproject" the result onto
the basis set) so addition, just like that of "standard" polynomials,
is simply "component-wise."

Examples
--------
>>> from numpy.polynomial import legendre as L
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> L.legadd(c1,c2)
array([4.,  4.,  4.])
- `leg2poly` (ID: a0013e88-8d9b-485d-a102-cad36d223c95): Convert a Legendre series to a polynomial.

Convert an array representing the coefficients of a Legendre series,
ordered from lowest degree to highest, to an array of the coefficients
of the equivalent polynomial (relative to the "standard" basis) ordered
from lowest to highest degree.

Parameters
----------
c : array_like
    1-D array containing the Legendre series coefficients, ordered
    from lowest order term to highest.

Returns
-------
pol : ndarray
    1-D array containing the coefficients of the equivalent polynomial
    (relative to the "standard" basis) ordered from lowest order term
    to highest.

See Also
--------
poly2leg

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy import polynomial as P
>>> c = P.Legendre(range(4))
>>> c
Legendre([0., 1., 2., 3.], domain=[-1.,  1.], window=[-1.,  1.], symbol='x')
>>> p = c.convert(kind=P.Polynomial)
>>> p
Polynomial([-1. , -3.5,  3. ,  7.5], domain=[-1.,  1.], window=[-1., ...
>>> P.legendre.leg2poly(range(4))
array([-1. , -3.5,  3. ,  7.5])
- `poly2lag` (ID: cffaac88-cd02-4a40-8222-8855a812dffb): poly2lag(pol)

Convert a polynomial to a Laguerre series.

Convert an array representing the coefficients of a polynomial (relative
to the "standard" basis) ordered from lowest degree to highest, to an
array of the coefficients of the equivalent Laguerre series, ordered
from lowest to highest degree.

Parameters
----------
pol : array_like
    1-D array containing the polynomial coefficients

Returns
-------
c : ndarray
    1-D array containing the coefficients of the equivalent Laguerre
    series.

See Also
--------
lag2poly

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.laguerre import poly2lag
>>> poly2lag(np.arange(4))
array([ 23., -63.,  58., -18.])
- `lagweight` (ID: 5284c8d5-b640-490b-a4ac-65f722dadb84): Weight function of the Laguerre polynomials.

The weight function is :math:`exp(-x)` and the interval of integration
is :math:`[0, \inf]`. The Laguerre polynomials are orthogonal, but not
normalized, with respect to this weight function.

Parameters
----------
x : array_like
   Values at which the weight function will be computed.

Returns
-------
w : ndarray
   The weight function at `x`.

Examples
--------
>>> from numpy.polynomial.laguerre import lagweight
>>> x = np.array([0, 1, 2])
>>> lagweight(x)
array([1.        , 0.36787944, 0.13533528])
- `lagvander3d` (ID: 6bb6d4db-b101-44d1-a231-451d5c5bf561): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y, z)``. If `l`, `m`, `n` are the given degrees in `x`, `y`, `z`,
then The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (m+1)(n+1)i + (n+1)j + k] = L_i(x)*L_j(y)*L_k(z),

where ``0 <= i <= l``, ``0 <= j <= m``, and ``0 <= j <= n``.  The leading
indices of `V` index the points ``(x, y, z)`` and the last index encodes
the degrees of the Laguerre polynomials.

If ``V = lagvander3d(x, y, z, [xdeg, ydeg, zdeg])``, then the columns
of `V` correspond to the elements of a 3-D coefficient array `c` of
shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

.. math:: c_{000}, c_{001}, c_{002},... , c_{010}, c_{011}, c_{012},...

and  ``np.dot(V, c.flat)`` and ``lagval3d(x, y, z, c)`` will be the
same up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 3-D Laguerre
series of the same degrees and sample points.

Parameters
----------
x, y, z : array_like
    Arrays of point coordinates, all of the same shape. The dtypes will
    be converted to either float64 or complex128 depending on whether
    any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg, z_deg].

Returns
-------
vander3d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)*(deg[2]+1)`.  The dtype will
    be the same as the converted `x`, `y`, and `z`.

See Also
--------
lagvander, lagvander3d, lagval2d, lagval3d

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.laguerre import lagvander3d
>>> x = np.array([0])
>>> y = np.array([2])
>>> z = np.array([0])
>>> lagvander3d(x, y, z, [2, 1, 3])
array([[ 1.,  1.,  1.,  1., -1., -1., -1., -1.,  1.,  1.,  1.,  1., -1.,
        -1., -1., -1.,  1.,  1.,  1.,  1., -1., -1., -1., -1.]])
- `lagvander2d` (ID: f5de8d20-9906-450d-866c-432c56287807): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y)``. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (deg[1] + 1)*i + j] = L_i(x) * L_j(y),

where ``0 <= i <= deg[0]`` and ``0 <= j <= deg[1]``. The leading indices of
`V` index the points ``(x, y)`` and the last index encodes the degrees of
the Laguerre polynomials.

If ``V = lagvander2d(x, y, [xdeg, ydeg])``, then the columns of `V`
correspond to the elements of a 2-D coefficient array `c` of shape
(xdeg + 1, ydeg + 1) in the order

.. math:: c_{00}, c_{01}, c_{02} ... , c_{10}, c_{11}, c_{12} ...

and ``np.dot(V, c.flat)`` and ``lagval2d(x, y, c)`` will be the same
up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 2-D Laguerre
series of the same degrees and sample points.

Parameters
----------
x, y : array_like
    Arrays of point coordinates, all of the same shape. The dtypes
    will be converted to either float64 or complex128 depending on
    whether any of the elements are complex. Scalars are converted to
    1-D arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg].

Returns
-------
vander2d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)`.  The dtype will be the same
    as the converted `x` and `y`.

See Also
--------
lagvander, lagvander3d, lagval2d, lagval3d

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.laguerre import lagvander2d
>>> x = np.array([0])
>>> y = np.array([2])
>>> lagvander2d(x, y, [2, 1])
array([[ 1., -1.,  1., -1.,  1., -1.]])
- `lagvander` (ID: 202e908e-3e19-4191-a362-ba772997cf04): Pseudo-Vandermonde matrix of given degree.

Returns the pseudo-Vandermonde matrix of degree `deg` and sample points
`x`. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., i] = L_i(x)

where ``0 <= i <= deg``. The leading indices of `V` index the elements of
`x` and the last index is the degree of the Laguerre polynomial.

If `c` is a 1-D array of coefficients of length ``n + 1`` and `V` is the
array ``V = lagvander(x, n)``, then ``np.dot(V, c)`` and
``lagval(x, c)`` are the same up to roundoff. This equivalence is
useful both for least squares fitting and for the evaluation of a large
number of Laguerre series of the same degree and sample points.

Parameters
----------
x : array_like
    Array of points. The dtype is converted to float64 or complex128
    depending on whether any of the elements are complex. If `x` is
    scalar it is converted to a 1-D array.
deg : int
    Degree of the resulting matrix.

Returns
-------
vander : ndarray
    The pseudo-Vandermonde matrix. The shape of the returned matrix is
    ``x.shape + (deg + 1,)``, where The last index is the degree of the
    corresponding Laguerre polynomial.  The dtype will be the same as
    the converted `x`.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.laguerre import lagvander
>>> x = np.array([0, 1, 2])
>>> lagvander(x, 3)
array([[ 1.        ,  1.        ,  1.        ,  1.        ],
       [ 1.        ,  0.        , -0.5       , -0.66666667],
       [ 1.        , -1.        , -1.        , -0.33333333]])
- `lagval3d` (ID: 4c0f47a9-0f8e-4249-8dbb-6cbfeef93287): Evaluate a 3-D Laguerre series at points (x, y, z).

This function returns the values:

.. math:: p(x,y,z) = \sum_{i,j,k} c_{i,j,k} * L_i(x) * L_j(y) * L_k(z)

The parameters `x`, `y`, and `z` are converted to arrays only if
they are tuples or a lists, otherwise they are treated as a scalars and
they must have the same shape after conversion. In either case, either
`x`, `y`, and `z` or their elements must support multiplication and
addition both with themselves and with the elements of `c`.

If `c` has fewer than 3 dimensions, ones are implicitly appended to its
shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape.

Parameters
----------
x, y, z : array_like, compatible object
    The three dimensional series is evaluated at the points
    ``(x, y, z)``, where `x`, `y`, and `z` must have the same shape.  If
    any of `x`, `y`, or `z` is a list or tuple, it is first converted
    to an ndarray, otherwise it is left unchanged and if it isn't an
    ndarray it is  treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j,k is contained in ``c[i,j,k]``. If `c` has dimension
    greater than 3 the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the multidimensional polynomial on points formed with
    triples of corresponding values from `x`, `y`, and `z`.

See Also
--------
lagval, lagval2d, laggrid2d, laggrid3d

Examples
--------
>>> from numpy.polynomial.laguerre import lagval3d
>>> c = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>>> lagval3d(1, 1, 2, c)
-1.0
- `lagval2d` (ID: d407ffb0-5f5d-4fab-b8e5-51d65fdff99c): Evaluate a 2-D Laguerre series at points (x, y).

This function returns the values:

.. math:: p(x,y) = \sum_{i,j} c_{i,j} * L_i(x) * L_j(y)

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars and they
must have the same shape after conversion. In either case, either `x`
and `y` or their elements must support multiplication and addition both
with themselves and with the elements of `c`.

If `c` is a 1-D array a one is implicitly appended to its shape to make
it 2-D. The shape of the result will be c.shape[2:] + x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points ``(x, y)``,
    where `x` and `y` must have the same shape. If `x` or `y` is a list
    or tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and if it isn't an ndarray it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term
    of multi-degree i,j is contained in ``c[i,j]``. If `c` has
    dimension greater than two the remaining indices enumerate multiple
    sets of coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points formed with
    pairs of corresponding values from `x` and `y`.

See Also
--------
lagval, laggrid2d, lagval3d, laggrid3d

Examples
--------
>>> from numpy.polynomial.laguerre import lagval2d
>>> c = [[1, 2],[3, 4]]
>>> lagval2d(1, 1, c)
1.0
- `lagval` (ID: 11f68884-b6ec-439d-a46e-f87197d77f04): Evaluate a Laguerre series at points x.

If `c` is of length ``n + 1``, this function returns the value:

.. math:: p(x) = c_0 * L_0(x) + c_1 * L_1(x) + ... + c_n * L_n(x)

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `c`.

If `c` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If
`c` is multidimensional, then the shape of the result depends on the
value of `tensor`. If `tensor` is true the shape will be c.shape[1:] +
x.shape. If `tensor` is false the shape will be c.shape[1:]. Note that
scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so
they should be avoided if efficiency is a concern.

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    themselves and with the elements of `c`.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree n are contained in c[n]. If `c` is multidimensional the
    remaining indices enumerate multiple polynomials. In the two
    dimensional case the coefficients may be thought of as stored in
    the columns of `c`.
tensor : boolean, optional
    If True, the shape of the coefficient array is extended with ones
    on the right, one for each dimension of `x`. Scalars have dimension 0
    for this action. The result is that every column of coefficients in
    `c` is evaluated for every element of `x`. If False, `x` is broadcast
    over the columns of `c` for the evaluation.  This keyword is useful
    when `c` is multidimensional. The default value is True.

Returns
-------
values : ndarray, algebra_like
    The shape of the return value is described above.

See Also
--------
lagval2d, laggrid2d, lagval3d, laggrid3d

Notes
-----
The evaluation uses Clenshaw recursion, aka synthetic division.

Examples
--------
>>> from numpy.polynomial.laguerre import lagval
>>> coef = [1, 2, 3]
>>> lagval(1, coef)
-0.5
>>> lagval([[1, 2],[3, 4]], coef)
array([[-0.5, -4. ],
       [-4.5, -2. ]])
- `lagsub` (ID: eaeea988-7a46-42b2-8df7-9d1d5db6b6d4): Subtract one Laguerre series from another.

Returns the difference of two Laguerre series `c1` - `c2`.  The
sequences of coefficients are from lowest order term to highest, i.e.,
[1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Laguerre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Laguerre series coefficients representing their difference.

See Also
--------
lagadd, lagmulx, lagmul, lagdiv, lagpow

Notes
-----
Unlike multiplication, division, etc., the difference of two Laguerre
series is a Laguerre series (without having to "reproject" the result
onto the basis set) so subtraction, just like that of "standard"
polynomials, is simply "component-wise."

Examples
--------
>>> from numpy.polynomial.laguerre import lagsub
>>> lagsub([1, 2, 3, 4], [1, 2, 3])
array([0.,  0.,  0.,  4.])
- `lagroots` (ID: 6bde7319-a326-49fb-8cc1-4aa9ed1e3972): Compute the roots of a Laguerre series.

Return the roots (a.k.a. "zeros") of the polynomial

.. math:: p(x) = \sum_i c[i] * L_i(x).

Parameters
----------
c : 1-D array_like
    1-D array of coefficients.

Returns
-------
out : ndarray
    Array of the roots of the series. If all the roots are real,
    then `out` is also real, otherwise it is complex.

See Also
--------
numpy.polynomial.polynomial.polyroots
numpy.polynomial.legendre.legroots
numpy.polynomial.chebyshev.chebroots
numpy.polynomial.hermite.hermroots
numpy.polynomial.hermite_e.hermeroots

Notes
-----
The root estimates are obtained as the eigenvalues of the companion
matrix, Roots far from the origin of the complex plane may have large
errors due to the numerical instability of the series for such
values. Roots with multiplicity greater than 1 will also show larger
errors as the value of the series near such points is relatively
insensitive to errors in the roots. Isolated roots near the origin can
be improved by a few iterations of Newton's method.

The Laguerre series basis polynomials aren't powers of `x` so the
results of this function may seem unintuitive.

Examples
--------
>>> from numpy.polynomial.laguerre import lagroots, lagfromroots
>>> coef = lagfromroots([0, 1, 2])
>>> coef
array([  2.,  -8.,  12.,  -6.])
>>> lagroots(coef)
array([-4.4408921e-16,  1.0000000e+00,  2.0000000e+00])
- `lagpow` (ID: 7aaf1850-34a0-4403-ba3b-be5a1274ce9d): Raise a Laguerre series to a power.

Returns the Laguerre series `c` raised to the power `pow`. The
argument `c` is a sequence of coefficients ordered from low to high.
i.e., [1,2,3] is the series  ``P_0 + 2*P_1 + 3*P_2.``

Parameters
----------
c : array_like
    1-D array of Laguerre series coefficients ordered from low to
    high.
pow : integer
    Power to which the series will be raised
maxpower : integer, optional
    Maximum power allowed. This is mainly to limit growth of the series
    to unmanageable size. Default is 16

Returns
-------
coef : ndarray
    Laguerre series of power.

See Also
--------
lagadd, lagsub, lagmulx, lagmul, lagdiv

Examples
--------
>>> from numpy.polynomial.laguerre import lagpow
>>> lagpow([1, 2, 3], 2)
array([ 14., -16.,  56., -72.,  54.])
- `lagmulx` (ID: d1093b45-b9a5-47d3-adaa-f5d227af6b71): Multiply a Laguerre series by x.

Multiply the Laguerre series `c` by x, where x is the independent
variable.


Parameters
----------
c : array_like
    1-D array of Laguerre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the result of the multiplication.

See Also
--------
lagadd, lagsub, lagmul, lagdiv, lagpow

Notes
-----
The multiplication uses the recursion relationship for Laguerre
polynomials in the form

.. math::

    xP_i(x) = (-(i + 1)*P_{i + 1}(x) + (2i + 1)P_{i}(x) - iP_{i - 1}(x))

Examples
--------
>>> from numpy.polynomial.laguerre import lagmulx
>>> lagmulx([1, 2, 3])
array([-1.,  -1.,  11.,  -9.])
- `lagmul` (ID: d560e1ff-a219-48ce-84c4-7ef1c2df1c8c): Multiply one Laguerre series by another.

Returns the product of two Laguerre series `c1` * `c2`.  The arguments
are sequences of coefficients, from lowest order "term" to highest,
e.g., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Laguerre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Laguerre series coefficients representing their product.

See Also
--------
lagadd, lagsub, lagmulx, lagdiv, lagpow

Notes
-----
In general, the (polynomial) product of two C-series results in terms
that are not in the Laguerre polynomial basis set.  Thus, to express
the product as a Laguerre series, it is necessary to "reproject" the
product onto said basis set, which may produce "unintuitive" (but
correct) results; see Examples section below.

Examples
--------
>>> from numpy.polynomial.laguerre import lagmul
>>> lagmul([1, 2, 3], [0, 1, 2])
array([  8., -13.,  38., -51.,  36.])
- `lagline` (ID: 827e3885-2970-47bc-9e97-24a43e2ca1b7): Laguerre series whose graph is a straight line.

Parameters
----------
off, scl : scalars
    The specified line is given by ``off + scl*x``.

Returns
-------
y : ndarray
    This module's representation of the Laguerre series for
    ``off + scl*x``.

See Also
--------
numpy.polynomial.polynomial.polyline
numpy.polynomial.chebyshev.chebline
numpy.polynomial.legendre.legline
numpy.polynomial.hermite.hermline
numpy.polynomial.hermite_e.hermeline

Examples
--------
>>> from numpy.polynomial.laguerre import lagline, lagval
>>> lagval(0,lagline(3, 2))
3.0
>>> lagval(1,lagline(3, 2))
5.0
- `lagint` (ID: a05346a6-c78d-4e61-b613-e92114753878): Integrate a Laguerre series.

Returns the Laguerre series coefficients `c` integrated `m` times from
`lbnd` along `axis`. At each iteration the resulting series is
**multiplied** by `scl` and an integration constant, `k`, is added.
The scaling factor is for use in a linear change of variable.  ("Buyer
beware": note that, depending on what one is doing, one may want `scl`
to be the reciprocal of what one might expect; for more information,
see the Notes section below.)  The argument `c` is an array of
coefficients from low to high degree along each axis, e.g., [1,2,3]
represents the series ``L_0 + 2*L_1 + 3*L_2`` while [[1,2],[1,2]]
represents ``1*L_0(x)*L_0(y) + 1*L_1(x)*L_0(y) + 2*L_0(x)*L_1(y) +
2*L_1(x)*L_1(y)`` if axis=0 is ``x`` and axis=1 is ``y``.


Parameters
----------
c : array_like
    Array of Laguerre series coefficients. If `c` is multidimensional
    the different axis correspond to different variables with the
    degree in each axis given by the corresponding index.
m : int, optional
    Order of integration, must be positive. (Default: 1)
k : {[], list, scalar}, optional
    Integration constant(s).  The value of the first integral at
    ``lbnd`` is the first value in the list, the value of the second
    integral at ``lbnd`` is the second value, etc.  If ``k == []`` (the
    default), all constants are set to zero.  If ``m == 1``, a single
    scalar can be given instead of a list.
lbnd : scalar, optional
    The lower bound of the integral. (Default: 0)
scl : scalar, optional
    Following each integration the result is *multiplied* by `scl`
    before the integration constant is added. (Default: 1)
axis : int, optional
    Axis over which the integral is taken. (Default: 0).

Returns
-------
S : ndarray
    Laguerre series coefficients of the integral.

Raises
------
ValueError
    If ``m < 0``, ``len(k) > m``, ``np.ndim(lbnd) != 0``, or
    ``np.ndim(scl) != 0``.

See Also
--------
lagder

Notes
-----
Note that the result of each integration is *multiplied* by `scl`.
Why is this important to note?  Say one is making a linear change of
variable :math:`u = ax + b` in an integral relative to `x`.  Then
:math:`dx = du/a`, so one will need to set `scl` equal to
:math:`1/a` - perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs
to be "reprojected" onto the C-series basis set.  Thus, typically,
the result of this function is "unintuitive," albeit correct; see
Examples section below.

Examples
--------
>>> from numpy.polynomial.laguerre import lagint
>>> lagint([1,2,3])
array([ 1.,  1.,  1., -3.])
>>> lagint([1,2,3], m=2)
array([ 1.,  0.,  0., -4.,  3.])
>>> lagint([1,2,3], k=1)
array([ 2.,  1.,  1., -3.])
>>> lagint([1,2,3], lbnd=-1)
array([11.5,  1. ,  1. , -3. ])
>>> lagint([1,2], m=2, k=[1,2], lbnd=-1)
array([ 11.16666667,  -5.        ,  -3.        ,   2.        ]) # may vary
- `laggrid3d` (ID: 80ef94a9-c15f-4081-b9d9-1a5bc250632f): Evaluate a 3-D Laguerre series on the Cartesian product of x, y, and z.

This function returns the values:

.. math:: p(a,b,c) = \sum_{i,j,k} c_{i,j,k} * L_i(a) * L_j(b) * L_k(c)

where the points ``(a, b, c)`` consist of all triples formed by taking
`a` from `x`, `b` from `y`, and `c` from `z`. The resulting points form
a grid with `x` in the first dimension, `y` in the second, and `z` in
the third.

The parameters `x`, `y`, and `z` are converted to arrays only if they
are tuples or a lists, otherwise they are treated as a scalars. In
either case, either `x`, `y`, and `z` or their elements must support
multiplication and addition both with themselves and with the elements
of `c`.

If `c` has fewer than three dimensions, ones are implicitly appended to
its shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape + y.shape + z.shape.

Parameters
----------
x, y, z : array_like, compatible objects
    The three dimensional series is evaluated at the points in the
    Cartesian product of `x`, `y`, and `z`.  If `x`, `y`, or `z` is a
    list or tuple, it is first converted to an ndarray, otherwise it is
    left unchanged and, if it isn't an ndarray, it is treated as a
    scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
lagval, lagval2d, laggrid2d, lagval3d

Examples
--------
>>> from numpy.polynomial.laguerre import laggrid3d
>>> c = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>>> laggrid3d([0, 1], [0, 1], [2, 4], c)
array([[[ -4., -44.],
        [ -2., -18.]],
       [[ -2., -14.],
        [ -1.,  -5.]]])
- `laggrid2d` (ID: abddfb2a-5059-4e1f-a97a-b7c32a295438): Evaluate a 2-D Laguerre series on the Cartesian product of x and y.

This function returns the values:

.. math:: p(a,b) = \sum_{i,j} c_{i,j} * L_i(a) * L_j(b)

where the points ``(a, b)`` consist of all pairs formed by taking
`a` from `x` and `b` from `y`. The resulting points form a grid with
`x` in the first dimension and `y` in the second.

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars. In either
case, either `x` and `y` or their elements must support multiplication
and addition both with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape + y.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points in the
    Cartesian product of `x` and `y`.  If `x` or `y` is a list or
    tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j is contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional Chebyshev series at points in the
    Cartesian product of `x` and `y`.

See Also
--------
lagval, lagval2d, lagval3d, laggrid3d

Examples
--------
>>> from numpy.polynomial.laguerre import laggrid2d
>>> c = [[1, 2], [3, 4]]
>>> laggrid2d([0, 1], [0, 1], c)
array([[10.,  4.],
       [ 3.,  1.]])
- `laggauss` (ID: aea97cd1-fe6c-487e-af17-089f45d483fc): Gauss-Laguerre quadrature.

Computes the sample points and weights for Gauss-Laguerre quadrature.
These sample points and weights will correctly integrate polynomials of
degree :math:`2*deg - 1` or less over the interval :math:`[0, \inf]`
with the weight function :math:`f(x) = \exp(-x)`.

Parameters
----------
deg : int
    Number of sample points and weights. It must be >= 1.

Returns
-------
x : ndarray
    1-D ndarray containing the sample points.
y : ndarray
    1-D ndarray containing the weights.

Notes
-----
The results have only been tested up to degree 100 higher degrees may
be problematic. The weights are determined by using the fact that

.. math:: w_k = c / (L'_n(x_k) * L_{n-1}(x_k))

where :math:`c` is a constant independent of :math:`k` and :math:`x_k`
is the k'th root of :math:`L_n`, and then scaling the results to get
the right value when integrating 1.

Examples
--------
>>> from numpy.polynomial.laguerre import laggauss
>>> laggauss(2)
(array([0.58578644, 3.41421356]), array([0.85355339, 0.14644661]))
- `lagfromroots` (ID: 77e5add6-7a6c-438e-8654-28030c965ba6): Generate a Laguerre series with given roots.

The function returns the coefficients of the polynomial

.. math:: p(x) = (x - r_0) * (x - r_1) * ... * (x - r_n),

in Laguerre form, where the :math:`r_n` are the roots specified in `roots`.
If a zero has multiplicity n, then it must appear in `roots` n times.
For instance, if 2 is a root of multiplicity three and 3 is a root of
multiplicity 2, then `roots` looks something like [2, 2, 2, 3, 3]. The
roots can appear in any order.

If the returned coefficients are `c`, then

.. math:: p(x) = c_0 + c_1 * L_1(x) + ... +  c_n * L_n(x)

The coefficient of the last term is not generally 1 for monic
polynomials in Laguerre form.

Parameters
----------
roots : array_like
    Sequence containing the roots.

Returns
-------
out : ndarray
    1-D array of coefficients.  If all roots are real then `out` is a
    real array, if some of the roots are complex, then `out` is complex
    even if all the coefficients in the result are real (see Examples
    below).

See Also
--------
numpy.polynomial.polynomial.polyfromroots
numpy.polynomial.legendre.legfromroots
numpy.polynomial.chebyshev.chebfromroots
numpy.polynomial.hermite.hermfromroots
numpy.polynomial.hermite_e.hermefromroots

Examples
--------
>>> from numpy.polynomial.laguerre import lagfromroots, lagval
>>> coef = lagfromroots((-1, 0, 1))
>>> lagval((-1, 0, 1), coef)
array([0.,  0.,  0.])
>>> coef = lagfromroots((-1j, 1j))
>>> lagval((-1j, 1j), coef)
array([0.+0.j, 0.+0.j])
- `lagfit` (ID: b6979bd3-d5a9-41b2-900c-c376ecc31961): Least squares fit of Laguerre series to data.

Return the coefficients of a Laguerre series of degree `deg` that is the
least squares fit to the data values `y` given at points `x`. If `y` is
1-D the returned coefficients will also be 1-D. If `y` is 2-D multiple
fits are done, one for each column of `y`, and the resulting
coefficients are stored in the corresponding columns of a 2-D return.
The fitted polynomial(s) are in the form

.. math::  p(x) = c_0 + c_1 * L_1(x) + ... + c_n * L_n(x),

where ``n`` is `deg`.

Parameters
----------
x : array_like, shape (M,)
    x-coordinates of the M sample points ``(x[i], y[i])``.
y : array_like, shape (M,) or (M, K)
    y-coordinates of the sample points. Several data sets of sample
    points sharing the same x-coordinates can be fitted at once by
    passing in a 2D-array that contains one dataset per column.
deg : int or 1-D array_like
    Degree(s) of the fitting polynomials. If `deg` is a single integer
    all terms up to and including the `deg`'th term are included in the
    fit. For NumPy versions >= 1.11.0 a list of integers specifying the
    degrees of the terms to include may be used instead.
rcond : float, optional
    Relative condition number of the fit. Singular values smaller than
    this relative to the largest singular value will be ignored. The
    default value is len(x)*eps, where eps is the relative precision of
    the float type, about 2e-16 in most cases.
full : bool, optional
    Switch determining nature of return value. When it is False (the
    default) just the coefficients are returned, when True diagnostic
    information from the singular value decomposition is also returned.
w : array_like, shape (`M`,), optional
    Weights. If not None, the weight ``w[i]`` applies to the unsquared
    residual ``y[i] - y_hat[i]`` at ``x[i]``. Ideally the weights are
    chosen so that the errors of the products ``w[i]*y[i]`` all have the
    same variance.  When using inverse-variance weighting, use
    ``w[i] = 1/sigma(y[i])``.  The default value is None.

Returns
-------
coef : ndarray, shape (M,) or (M, K)
    Laguerre coefficients ordered from low to high. If `y` was 2-D,
    the coefficients for the data in column *k*  of `y` are in column
    *k*.

[residuals, rank, singular_values, rcond] : list
    These values are only returned if ``full == True``

    - residuals -- sum of squared residuals of the least squares fit
    - rank -- the numerical rank of the scaled Vandermonde matrix
    - singular_values -- singular values of the scaled Vandermonde matrix
    - rcond -- value of `rcond`.

    For more details, see `numpy.linalg.lstsq`.

Warns
-----
RankWarning
    The rank of the coefficient matrix in the least-squares fit is
    deficient. The warning is only raised if ``full == False``.  The
    warnings can be turned off by

    >>> import warnings
    >>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

See Also
--------
numpy.polynomial.polynomial.polyfit
numpy.polynomial.legendre.legfit
numpy.polynomial.chebyshev.chebfit
numpy.polynomial.hermite.hermfit
numpy.polynomial.hermite_e.hermefit
lagval : Evaluates a Laguerre series.
lagvander : pseudo Vandermonde matrix of Laguerre series.
lagweight : Laguerre weight function.
numpy.linalg.lstsq : Computes a least-squares fit from the matrix.
scipy.interpolate.UnivariateSpline : Computes spline fits.

Notes
-----
The solution is the coefficients of the Laguerre series ``p`` that
minimizes the sum of the weighted squared errors

.. math:: E = \sum_j w_j^2 * |y_j - p(x_j)|^2,

where the :math:`w_j` are the weights. This problem is solved by
setting up as the (typically) overdetermined matrix equation

.. math:: V(x) * c = w * y,

where ``V`` is the weighted pseudo Vandermonde matrix of `x`, ``c`` are the
coefficients to be solved for, `w` are the weights, and `y` are the
observed values.  This equation is then solved using the singular value
decomposition of ``V``.

If some of the singular values of `V` are so small that they are
neglected, then a `~exceptions.RankWarning` will be issued. This means that
the coefficient values may be poorly determined. Using a lower order fit
will usually get rid of the warning.  The `rcond` parameter can also be
set to a value smaller than its default, but the resulting fit may be
spurious and have large contributions from roundoff error.

Fits using Laguerre series are probably most useful when the data can
be approximated by ``sqrt(w(x)) * p(x)``, where ``w(x)`` is the Laguerre
weight. In that case the weight ``sqrt(w(x[i]))`` should be used
together with data values ``y[i]/sqrt(w(x[i]))``. The weight function is
available as `lagweight`.

References
----------
.. [1] Wikipedia, "Curve fitting",
       https://en.wikipedia.org/wiki/Curve_fitting

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.laguerre import lagfit, lagval
>>> x = np.linspace(0, 10)
>>> rng = np.random.default_rng()
>>> err = rng.normal(scale=1./10, size=len(x))
>>> y = lagval(x, [1, 2, 3]) + err
>>> lagfit(x, y, 2)
array([1.00578369, 1.99417356, 2.99827656]) # may vary
- `lagdiv` (ID: 4b2df9ec-9370-4728-90e0-d4374578a3f6): Divide one Laguerre series by another.

Returns the quotient-with-remainder of two Laguerre series
`c1` / `c2`.  The arguments are sequences of coefficients from lowest
order "term" to highest, e.g., [1,2,3] represents the series
``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Laguerre series coefficients ordered from low to
    high.

Returns
-------
[quo, rem] : ndarrays
    Of Laguerre series coefficients representing the quotient and
    remainder.

See Also
--------
lagadd, lagsub, lagmulx, lagmul, lagpow

Notes
-----
In general, the (polynomial) division of one Laguerre series by another
results in quotient and remainder terms that are not in the Laguerre
polynomial basis set.  Thus, to express these results as a Laguerre
series, it is necessary to "reproject" the results onto the Laguerre
basis set, which may produce "unintuitive" (but correct) results; see
Examples section below.

Examples
--------
>>> from numpy.polynomial.laguerre import lagdiv
>>> lagdiv([  8., -13.,  38., -51.,  36.], [0, 1, 2])
(array([1., 2., 3.]), array([0.]))
>>> lagdiv([  9., -12.,  38., -51.,  36.], [0, 1, 2])
(array([1., 2., 3.]), array([1., 1.]))
- `lagder` (ID: 4ce9b151-291f-410a-bae2-23839563f956): Differentiate a Laguerre series.

Returns the Laguerre series coefficients `c` differentiated `m` times
along `axis`.  At each iteration the result is multiplied by `scl` (the
scaling factor is for use in a linear change of variable). The argument
`c` is an array of coefficients from low to high degree along each
axis, e.g., [1,2,3] represents the series ``1*L_0 + 2*L_1 + 3*L_2``
while [[1,2],[1,2]] represents ``1*L_0(x)*L_0(y) + 1*L_1(x)*L_0(y) +
2*L_0(x)*L_1(y) + 2*L_1(x)*L_1(y)`` if axis=0 is ``x`` and axis=1 is
``y``.

Parameters
----------
c : array_like
    Array of Laguerre series coefficients. If `c` is multidimensional
    the different axis correspond to different variables with the
    degree in each axis given by the corresponding index.
m : int, optional
    Number of derivatives taken, must be non-negative. (Default: 1)
scl : scalar, optional
    Each differentiation is multiplied by `scl`.  The end result is
    multiplication by ``scl**m``.  This is for use in a linear change of
    variable. (Default: 1)
axis : int, optional
    Axis over which the derivative is taken. (Default: 0).

Returns
-------
der : ndarray
    Laguerre series of the derivative.

See Also
--------
lagint

Notes
-----
In general, the result of differentiating a Laguerre series does not
resemble the same operation on a power series. Thus the result of this
function may be "unintuitive," albeit correct; see Examples section
below.

Examples
--------
>>> from numpy.polynomial.laguerre import lagder
>>> lagder([ 1.,  1.,  1., -3.])
array([1.,  2.,  3.])
>>> lagder([ 1.,  0.,  0., -4.,  3.], m=2)
array([1.,  2.,  3.])
- `lagcompanion` (ID: 29fd93d1-49c8-4adf-90aa-90edd840aae7): Return the companion matrix of c.

The usual companion matrix of the Laguerre polynomials is already
symmetric when `c` is a basis Laguerre polynomial, so no scaling is
applied.

Parameters
----------
c : array_like
    1-D array of Laguerre series coefficients ordered from low to high
    degree.

Returns
-------
mat : ndarray
    Companion matrix of dimensions (deg, deg).

Examples
--------
>>> from numpy.polynomial.laguerre import lagcompanion
>>> lagcompanion([1, 2, 3])
array([[ 1.        , -0.33333333],
       [-1.        ,  4.33333333]])
- `lagadd` (ID: 5c28ab70-81ae-4fe5-976a-94a8950ecf8e): Add one Laguerre series to another.

Returns the sum of two Laguerre series `c1` + `c2`.  The arguments
are sequences of coefficients ordered from lowest order term to
highest, i.e., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Laguerre series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the Laguerre series of their sum.

See Also
--------
lagsub, lagmulx, lagmul, lagdiv, lagpow

Notes
-----
Unlike multiplication, division, etc., the sum of two Laguerre series
is a Laguerre series (without having to "reproject" the result onto
the basis set) so addition, just like that of "standard" polynomials,
is simply "component-wise."

Examples
--------
>>> from numpy.polynomial.laguerre import lagadd
>>> lagadd([1, 2, 3], [1, 2, 3, 4])
array([2.,  4.,  6.,  4.])
- `lag2poly` (ID: bb4e6677-39f0-429c-bb94-ec608be673d6): Convert a Laguerre series to a polynomial.

Convert an array representing the coefficients of a Laguerre series,
ordered from lowest degree to highest, to an array of the coefficients
of the equivalent polynomial (relative to the "standard" basis) ordered
from lowest to highest degree.

Parameters
----------
c : array_like
    1-D array containing the Laguerre series coefficients, ordered
    from lowest order term to highest.

Returns
-------
pol : ndarray
    1-D array containing the coefficients of the equivalent polynomial
    (relative to the "standard" basis) ordered from lowest order term
    to highest.

See Also
--------
poly2lag

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy.polynomial.laguerre import lag2poly
>>> lag2poly([ 23., -63.,  58., -18.])
array([0., 1., 2., 3.])
- `poly2herme` (ID: 0317171a-9aee-45de-a27e-602755de4ae8): poly2herme(pol)

Convert a polynomial to a Hermite series.

Convert an array representing the coefficients of a polynomial (relative
to the "standard" basis) ordered from lowest degree to highest, to an
array of the coefficients of the equivalent Hermite series, ordered
from lowest to highest degree.

Parameters
----------
pol : array_like
    1-D array containing the polynomial coefficients

Returns
-------
c : ndarray
    1-D array containing the coefficients of the equivalent Hermite
    series.

See Also
--------
herme2poly

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite_e import poly2herme
>>> poly2herme(np.arange(4))
array([  2.,  10.,   2.,   3.])
- `hermeweight` (ID: 846cf015-0866-4987-9d27-2616e5888100): Weight function of the Hermite_e polynomials.

The weight function is :math:`\exp(-x^2/2)` and the interval of
integration is :math:`[-\inf, \inf]`. the HermiteE polynomials are
orthogonal, but not normalized, with respect to this weight function.

Parameters
----------
x : array_like
   Values at which the weight function will be computed.

Returns
-------
w : ndarray
   The weight function at `x`.
- `hermevander3d` (ID: 23278c25-b048-422c-a8e2-860bbb4ca0b7): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y, z)``. If `l`, `m`, `n` are the given degrees in `x`, `y`, `z`,
then Hehe pseudo-Vandermonde matrix is defined by

.. math:: V[..., (m+1)(n+1)i + (n+1)j + k] = He_i(x)*He_j(y)*He_k(z),

where ``0 <= i <= l``, ``0 <= j <= m``, and ``0 <= j <= n``.  The leading
indices of `V` index the points ``(x, y, z)`` and the last index encodes
the degrees of the HermiteE polynomials.

If ``V = hermevander3d(x, y, z, [xdeg, ydeg, zdeg])``, then the columns
of `V` correspond to the elements of a 3-D coefficient array `c` of
shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

.. math:: c_{000}, c_{001}, c_{002},... , c_{010}, c_{011}, c_{012},...

and  ``np.dot(V, c.flat)`` and ``hermeval3d(x, y, z, c)`` will be the
same up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 3-D HermiteE
series of the same degrees and sample points.

Parameters
----------
x, y, z : array_like
    Arrays of point coordinates, all of the same shape. The dtypes will
    be converted to either float64 or complex128 depending on whether
    any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg, z_deg].

Returns
-------
vander3d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)*(deg[2]+1)`.  The dtype will
    be the same as the converted `x`, `y`, and `z`.

See Also
--------
hermevander, hermevander3d, hermeval2d, hermeval3d
- `hermevander2d` (ID: a7c5454d-838e-4756-a04f-56078205f627): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y)``. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (deg[1] + 1)*i + j] = He_i(x) * He_j(y),

where ``0 <= i <= deg[0]`` and ``0 <= j <= deg[1]``. The leading indices of
`V` index the points ``(x, y)`` and the last index encodes the degrees of
the HermiteE polynomials.

If ``V = hermevander2d(x, y, [xdeg, ydeg])``, then the columns of `V`
correspond to the elements of a 2-D coefficient array `c` of shape
(xdeg + 1, ydeg + 1) in the order

.. math:: c_{00}, c_{01}, c_{02} ... , c_{10}, c_{11}, c_{12} ...

and ``np.dot(V, c.flat)`` and ``hermeval2d(x, y, c)`` will be the same
up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 2-D HermiteE
series of the same degrees and sample points.

Parameters
----------
x, y : array_like
    Arrays of point coordinates, all of the same shape. The dtypes
    will be converted to either float64 or complex128 depending on
    whether any of the elements are complex. Scalars are converted to
    1-D arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg].

Returns
-------
vander2d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)`.  The dtype will be the same
    as the converted `x` and `y`.

See Also
--------
hermevander, hermevander3d, hermeval2d, hermeval3d
- `hermevander` (ID: 40e7c806-afaf-4b38-99c1-212e6a355453): Pseudo-Vandermonde matrix of given degree.

Returns the pseudo-Vandermonde matrix of degree `deg` and sample points
`x`. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., i] = He_i(x),

where ``0 <= i <= deg``. The leading indices of `V` index the elements of
`x` and the last index is the degree of the HermiteE polynomial.

If `c` is a 1-D array of coefficients of length ``n + 1`` and `V` is the
array ``V = hermevander(x, n)``, then ``np.dot(V, c)`` and
``hermeval(x, c)`` are the same up to roundoff. This equivalence is
useful both for least squares fitting and for the evaluation of a large
number of HermiteE series of the same degree and sample points.

Parameters
----------
x : array_like
    Array of points. The dtype is converted to float64 or complex128
    depending on whether any of the elements are complex. If `x` is
    scalar it is converted to a 1-D array.
deg : int
    Degree of the resulting matrix.

Returns
-------
vander : ndarray
    The pseudo-Vandermonde matrix. The shape of the returned matrix is
    ``x.shape + (deg + 1,)``, where The last index is the degree of the
    corresponding HermiteE polynomial.  The dtype will be the same as
    the converted `x`.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite_e import hermevander
>>> x = np.array([-1, 0, 1])
>>> hermevander(x, 3)
array([[ 1., -1.,  0.,  2.],
       [ 1.,  0., -1., -0.],
       [ 1.,  1.,  0., -2.]])
- `hermeval3d` (ID: a46c4152-1205-4247-913d-fa17b82d5b3f): Evaluate a 3-D Hermite_e series at points (x, y, z).

This function returns the values:

.. math:: p(x,y,z) = \sum_{i,j,k} c_{i,j,k} * He_i(x) * He_j(y) * He_k(z)

The parameters `x`, `y`, and `z` are converted to arrays only if
they are tuples or a lists, otherwise they are treated as a scalars and
they must have the same shape after conversion. In either case, either
`x`, `y`, and `z` or their elements must support multiplication and
addition both with themselves and with the elements of `c`.

If `c` has fewer than 3 dimensions, ones are implicitly appended to its
shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape.

Parameters
----------
x, y, z : array_like, compatible object
    The three dimensional series is evaluated at the points
    `(x, y, z)`, where `x`, `y`, and `z` must have the same shape.  If
    any of `x`, `y`, or `z` is a list or tuple, it is first converted
    to an ndarray, otherwise it is left unchanged and if it isn't an
    ndarray it is  treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j,k is contained in ``c[i,j,k]``. If `c` has dimension
    greater than 3 the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the multidimensional polynomial on points formed with
    triples of corresponding values from `x`, `y`, and `z`.

See Also
--------
hermeval, hermeval2d, hermegrid2d, hermegrid3d
- `hermeval2d` (ID: a2541d01-ce8c-42c5-b385-82779c33bbc9): Evaluate a 2-D HermiteE series at points (x, y).

This function returns the values:

.. math:: p(x,y) = \sum_{i,j} c_{i,j} * He_i(x) * He_j(y)

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars and they
must have the same shape after conversion. In either case, either `x`
and `y` or their elements must support multiplication and addition both
with themselves and with the elements of `c`.

If `c` is a 1-D array a one is implicitly appended to its shape to make
it 2-D. The shape of the result will be c.shape[2:] + x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points ``(x, y)``,
    where `x` and `y` must have the same shape. If `x` or `y` is a list
    or tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and if it isn't an ndarray it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term
    of multi-degree i,j is contained in ``c[i,j]``. If `c` has
    dimension greater than two the remaining indices enumerate multiple
    sets of coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points formed with
    pairs of corresponding values from `x` and `y`.

See Also
--------
hermeval, hermegrid2d, hermeval3d, hermegrid3d
- `hermeval` (ID: ae8b47e4-0119-46a9-93ec-fc27f7e9f86a): Evaluate an HermiteE series at points x.

If `c` is of length ``n + 1``, this function returns the value:

.. math:: p(x) = c_0 * He_0(x) + c_1 * He_1(x) + ... + c_n * He_n(x)

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `c`.

If `c` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If
`c` is multidimensional, then the shape of the result depends on the
value of `tensor`. If `tensor` is true the shape will be c.shape[1:] +
x.shape. If `tensor` is false the shape will be c.shape[1:]. Note that
scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so
they should be avoided if efficiency is a concern.

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    with themselves and with the elements of `c`.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree n are contained in c[n]. If `c` is multidimensional the
    remaining indices enumerate multiple polynomials. In the two
    dimensional case the coefficients may be thought of as stored in
    the columns of `c`.
tensor : boolean, optional
    If True, the shape of the coefficient array is extended with ones
    on the right, one for each dimension of `x`. Scalars have dimension 0
    for this action. The result is that every column of coefficients in
    `c` is evaluated for every element of `x`. If False, `x` is broadcast
    over the columns of `c` for the evaluation.  This keyword is useful
    when `c` is multidimensional. The default value is True.

Returns
-------
values : ndarray, algebra_like
    The shape of the return value is described above.

See Also
--------
hermeval2d, hermegrid2d, hermeval3d, hermegrid3d

Notes
-----
The evaluation uses Clenshaw recursion, aka synthetic division.

Examples
--------
>>> from numpy.polynomial.hermite_e import hermeval
>>> coef = [1,2,3]
>>> hermeval(1, coef)
3.0
>>> hermeval([[1,2],[3,4]], coef)
array([[ 3., 14.],
       [31., 54.]])
- `hermesub` (ID: cbe8d6c5-8849-489b-b82d-ec606f8ef376): Subtract one Hermite series from another.

Returns the difference of two Hermite series `c1` - `c2`.  The
sequences of coefficients are from lowest order term to highest, i.e.,
[1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Hermite series coefficients representing their difference.

See Also
--------
hermeadd, hermemulx, hermemul, hermediv, hermepow

Notes
-----
Unlike multiplication, division, etc., the difference of two Hermite
series is a Hermite series (without having to "reproject" the result
onto the basis set) so subtraction, just like that of "standard"
polynomials, is simply "component-wise."

Examples
--------
>>> from numpy.polynomial.hermite_e import hermesub
>>> hermesub([1, 2, 3, 4], [1, 2, 3])
array([0., 0., 0., 4.])
- `hermeroots` (ID: 96b628fb-383d-4198-bcec-7de8e9a5c514): Compute the roots of a HermiteE series.

Return the roots (a.k.a. "zeros") of the polynomial

.. math:: p(x) = \sum_i c[i] * He_i(x).

Parameters
----------
c : 1-D array_like
    1-D array of coefficients.

Returns
-------
out : ndarray
    Array of the roots of the series. If all the roots are real,
    then `out` is also real, otherwise it is complex.

See Also
--------
numpy.polynomial.polynomial.polyroots
numpy.polynomial.legendre.legroots
numpy.polynomial.laguerre.lagroots
numpy.polynomial.hermite.hermroots
numpy.polynomial.chebyshev.chebroots

Notes
-----
The root estimates are obtained as the eigenvalues of the companion
matrix, Roots far from the origin of the complex plane may have large
errors due to the numerical instability of the series for such
values. Roots with multiplicity greater than 1 will also show larger
errors as the value of the series near such points is relatively
insensitive to errors in the roots. Isolated roots near the origin can
be improved by a few iterations of Newton's method.

The HermiteE series basis polynomials aren't powers of `x` so the
results of this function may seem unintuitive.

Examples
--------
>>> from numpy.polynomial.hermite_e import hermeroots, hermefromroots
>>> coef = hermefromroots([-1, 0, 1])
>>> coef
array([0., 2., 0., 1.])
>>> hermeroots(coef)
array([-1.,  0.,  1.]) # may vary
- `hermepow` (ID: 8f36c730-64bc-433b-87f0-f05e5b3a9418): Raise a Hermite series to a power.

Returns the Hermite series `c` raised to the power `pow`. The
argument `c` is a sequence of coefficients ordered from low to high.
i.e., [1,2,3] is the series  ``P_0 + 2*P_1 + 3*P_2.``

Parameters
----------
c : array_like
    1-D array of Hermite series coefficients ordered from low to
    high.
pow : integer
    Power to which the series will be raised
maxpower : integer, optional
    Maximum power allowed. This is mainly to limit growth of the series
    to unmanageable size. Default is 16

Returns
-------
coef : ndarray
    Hermite series of power.

See Also
--------
hermeadd, hermesub, hermemulx, hermemul, hermediv

Examples
--------
>>> from numpy.polynomial.hermite_e import hermepow
>>> hermepow([1, 2, 3], 2)
array([23.,  28.,  46.,  12.,   9.])
- `hermemulx` (ID: e1447cde-ed56-4360-bcd8-af07996395da): Multiply a Hermite series by x.

Multiply the Hermite series `c` by x, where x is the independent
variable.


Parameters
----------
c : array_like
    1-D array of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the result of the multiplication.

See Also
--------
hermeadd, hermesub, hermemul, hermediv, hermepow

Notes
-----
The multiplication uses the recursion relationship for Hermite
polynomials in the form

.. math::

    xP_i(x) = (P_{i + 1}(x) + iP_{i - 1}(x)))

Examples
--------
>>> from numpy.polynomial.hermite_e import hermemulx
>>> hermemulx([1, 2, 3])
array([2.,  7.,  2.,  3.])
- `hermemul` (ID: 183946e7-4086-4522-8d8d-e55ae828f8cf): Multiply one Hermite series by another.

Returns the product of two Hermite series `c1` * `c2`.  The arguments
are sequences of coefficients, from lowest order "term" to highest,
e.g., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Hermite series coefficients representing their product.

See Also
--------
hermeadd, hermesub, hermemulx, hermediv, hermepow

Notes
-----
In general, the (polynomial) product of two C-series results in terms
that are not in the Hermite polynomial basis set.  Thus, to express
the product as a Hermite series, it is necessary to "reproject" the
product onto said basis set, which may produce "unintuitive" (but
correct) results; see Examples section below.

Examples
--------
>>> from numpy.polynomial.hermite_e import hermemul
>>> hermemul([1, 2, 3], [0, 1, 2])
array([14.,  15.,  28.,   7.,   6.])
- `hermeline` (ID: 2cb85ebd-6c2a-449c-af0e-d3584acbf2ac): Hermite series whose graph is a straight line.

Parameters
----------
off, scl : scalars
    The specified line is given by ``off + scl*x``.

Returns
-------
y : ndarray
    This module's representation of the Hermite series for
    ``off + scl*x``.

See Also
--------
numpy.polynomial.polynomial.polyline
numpy.polynomial.chebyshev.chebline
numpy.polynomial.legendre.legline
numpy.polynomial.laguerre.lagline
numpy.polynomial.hermite.hermline

Examples
--------
>>> from numpy.polynomial.hermite_e import hermeline
>>> from numpy.polynomial.hermite_e import hermeline, hermeval
>>> hermeval(0,hermeline(3, 2))
3.0
>>> hermeval(1,hermeline(3, 2))
5.0
- `hermeint` (ID: f5a92d9a-01e4-4da4-abf2-ae82e963639a): Integrate a Hermite_e series.

Returns the Hermite_e series coefficients `c` integrated `m` times from
`lbnd` along `axis`. At each iteration the resulting series is
**multiplied** by `scl` and an integration constant, `k`, is added.
The scaling factor is for use in a linear change of variable.  ("Buyer
beware": note that, depending on what one is doing, one may want `scl`
to be the reciprocal of what one might expect; for more information,
see the Notes section below.)  The argument `c` is an array of
coefficients from low to high degree along each axis, e.g., [1,2,3]
represents the series ``H_0 + 2*H_1 + 3*H_2`` while [[1,2],[1,2]]
represents ``1*H_0(x)*H_0(y) + 1*H_1(x)*H_0(y) + 2*H_0(x)*H_1(y) +
2*H_1(x)*H_1(y)`` if axis=0 is ``x`` and axis=1 is ``y``.

Parameters
----------
c : array_like
    Array of Hermite_e series coefficients. If c is multidimensional
    the different axis correspond to different variables with the
    degree in each axis given by the corresponding index.
m : int, optional
    Order of integration, must be positive. (Default: 1)
k : {[], list, scalar}, optional
    Integration constant(s).  The value of the first integral at
    ``lbnd`` is the first value in the list, the value of the second
    integral at ``lbnd`` is the second value, etc.  If ``k == []`` (the
    default), all constants are set to zero.  If ``m == 1``, a single
    scalar can be given instead of a list.
lbnd : scalar, optional
    The lower bound of the integral. (Default: 0)
scl : scalar, optional
    Following each integration the result is *multiplied* by `scl`
    before the integration constant is added. (Default: 1)
axis : int, optional
    Axis over which the integral is taken. (Default: 0).

Returns
-------
S : ndarray
    Hermite_e series coefficients of the integral.

Raises
------
ValueError
    If ``m < 0``, ``len(k) > m``, ``np.ndim(lbnd) != 0``, or
    ``np.ndim(scl) != 0``.

See Also
--------
hermeder

Notes
-----
Note that the result of each integration is *multiplied* by `scl`.
Why is this important to note?  Say one is making a linear change of
variable :math:`u = ax + b` in an integral relative to `x`.  Then
:math:`dx = du/a`, so one will need to set `scl` equal to
:math:`1/a` - perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs
to be "reprojected" onto the C-series basis set.  Thus, typically,
the result of this function is "unintuitive," albeit correct; see
Examples section below.

Examples
--------
>>> from numpy.polynomial.hermite_e import hermeint
>>> hermeint([1, 2, 3]) # integrate once, value 0 at 0.
array([1., 1., 1., 1.])
>>> hermeint([1, 2, 3], m=2) # integrate twice, value & deriv 0 at 0
array([-0.25      ,  1.        ,  0.5       ,  0.33333333,  0.25      ]) # may vary
>>> hermeint([1, 2, 3], k=1) # integrate once, value 1 at 0.
array([2., 1., 1., 1.])
>>> hermeint([1, 2, 3], lbnd=-1) # integrate once, value 0 at -1
array([-1.,  1.,  1.,  1.])
>>> hermeint([1, 2, 3], m=2, k=[1, 2], lbnd=-1)
array([ 1.83333333,  0.        ,  0.5       ,  0.33333333,  0.25      ]) # may vary
- `hermegrid3d` (ID: 561f4888-a10b-4198-b76a-a4ac9921ac37): Evaluate a 3-D HermiteE series on the Cartesian product of x, y, and z.

This function returns the values:

.. math:: p(a,b,c) = \sum_{i,j,k} c_{i,j,k} * He_i(a) * He_j(b) * He_k(c)

where the points ``(a, b, c)`` consist of all triples formed by taking
`a` from `x`, `b` from `y`, and `c` from `z`. The resulting points form
a grid with `x` in the first dimension, `y` in the second, and `z` in
the third.

The parameters `x`, `y`, and `z` are converted to arrays only if they
are tuples or a lists, otherwise they are treated as a scalars. In
either case, either `x`, `y`, and `z` or their elements must support
multiplication and addition both with themselves and with the elements
of `c`.

If `c` has fewer than three dimensions, ones are implicitly appended to
its shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape + y.shape + z.shape.

Parameters
----------
x, y, z : array_like, compatible objects
    The three dimensional series is evaluated at the points in the
    Cartesian product of `x`, `y`, and `z`.  If `x`, `y`, or `z` is a
    list or tuple, it is first converted to an ndarray, otherwise it is
    left unchanged and, if it isn't an ndarray, it is treated as a
    scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
hermeval, hermeval2d, hermegrid2d, hermeval3d
- `hermegrid2d` (ID: ef89abc2-196b-4843-8b72-2d6e9407dd4a): Evaluate a 2-D HermiteE series on the Cartesian product of x and y.

This function returns the values:

.. math:: p(a,b) = \sum_{i,j} c_{i,j} * H_i(a) * H_j(b)

where the points ``(a, b)`` consist of all pairs formed by taking
`a` from `x` and `b` from `y`. The resulting points form a grid with
`x` in the first dimension and `y` in the second.

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars. In either
case, either `x` and `y` or their elements must support multiplication
and addition both with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points in the
    Cartesian product of `x` and `y`.  If `x` or `y` is a list or
    tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
hermeval, hermeval2d, hermeval3d, hermegrid3d
- `hermegauss` (ID: 93bcb333-a59d-4ef8-bbf7-3540332d381b): Gauss-HermiteE quadrature.

Computes the sample points and weights for Gauss-HermiteE quadrature.
These sample points and weights will correctly integrate polynomials of
degree :math:`2*deg - 1` or less over the interval :math:`[-\inf, \inf]`
with the weight function :math:`f(x) = \exp(-x^2/2)`.

Parameters
----------
deg : int
    Number of sample points and weights. It must be >= 1.

Returns
-------
x : ndarray
    1-D ndarray containing the sample points.
y : ndarray
    1-D ndarray containing the weights.

Notes
-----
The results have only been tested up to degree 100, higher degrees may
be problematic. The weights are determined by using the fact that

.. math:: w_k = c / (He'_n(x_k) * He_{n-1}(x_k))

where :math:`c` is a constant independent of :math:`k` and :math:`x_k`
is the k'th root of :math:`He_n`, and then scaling the results to get
the right value when integrating 1.
- `hermefromroots` (ID: d7c526bd-8b76-469f-a50f-0f047dffe2b5): Generate a HermiteE series with given roots.

The function returns the coefficients of the polynomial

.. math:: p(x) = (x - r_0) * (x - r_1) * ... * (x - r_n),

in HermiteE form, where the :math:`r_n` are the roots specified in `roots`.
If a zero has multiplicity n, then it must appear in `roots` n times.
For instance, if 2 is a root of multiplicity three and 3 is a root of
multiplicity 2, then `roots` looks something like [2, 2, 2, 3, 3]. The
roots can appear in any order.

If the returned coefficients are `c`, then

.. math:: p(x) = c_0 + c_1 * He_1(x) + ... +  c_n * He_n(x)

The coefficient of the last term is not generally 1 for monic
polynomials in HermiteE form.

Parameters
----------
roots : array_like
    Sequence containing the roots.

Returns
-------
out : ndarray
    1-D array of coefficients.  If all roots are real then `out` is a
    real array, if some of the roots are complex, then `out` is complex
    even if all the coefficients in the result are real (see Examples
    below).

See Also
--------
numpy.polynomial.polynomial.polyfromroots
numpy.polynomial.legendre.legfromroots
numpy.polynomial.laguerre.lagfromroots
numpy.polynomial.hermite.hermfromroots
numpy.polynomial.chebyshev.chebfromroots

Examples
--------
>>> from numpy.polynomial.hermite_e import hermefromroots, hermeval
>>> coef = hermefromroots((-1, 0, 1))
>>> hermeval((-1, 0, 1), coef)
array([0., 0., 0.])
>>> coef = hermefromroots((-1j, 1j))
>>> hermeval((-1j, 1j), coef)
array([0.+0.j, 0.+0.j])
- `hermefit` (ID: 037902fb-c3e7-4624-a831-aa05377d08f8): Least squares fit of Hermite series to data.

Return the coefficients of a HermiteE series of degree `deg` that is
the least squares fit to the data values `y` given at points `x`. If
`y` is 1-D the returned coefficients will also be 1-D. If `y` is 2-D
multiple fits are done, one for each column of `y`, and the resulting
coefficients are stored in the corresponding columns of a 2-D return.
The fitted polynomial(s) are in the form

.. math::  p(x) = c_0 + c_1 * He_1(x) + ... + c_n * He_n(x),

where `n` is `deg`.

Parameters
----------
x : array_like, shape (M,)
    x-coordinates of the M sample points ``(x[i], y[i])``.
y : array_like, shape (M,) or (M, K)
    y-coordinates of the sample points. Several data sets of sample
    points sharing the same x-coordinates can be fitted at once by
    passing in a 2D-array that contains one dataset per column.
deg : int or 1-D array_like
    Degree(s) of the fitting polynomials. If `deg` is a single integer
    all terms up to and including the `deg`'th term are included in the
    fit. For NumPy versions >= 1.11.0 a list of integers specifying the
    degrees of the terms to include may be used instead.
rcond : float, optional
    Relative condition number of the fit. Singular values smaller than
    this relative to the largest singular value will be ignored. The
    default value is len(x)*eps, where eps is the relative precision of
    the float type, about 2e-16 in most cases.
full : bool, optional
    Switch determining nature of return value. When it is False (the
    default) just the coefficients are returned, when True diagnostic
    information from the singular value decomposition is also returned.
w : array_like, shape (`M`,), optional
    Weights. If not None, the weight ``w[i]`` applies to the unsquared
    residual ``y[i] - y_hat[i]`` at ``x[i]``. Ideally the weights are
    chosen so that the errors of the products ``w[i]*y[i]`` all have the
    same variance.  When using inverse-variance weighting, use
    ``w[i] = 1/sigma(y[i])``.  The default value is None.

Returns
-------
coef : ndarray, shape (M,) or (M, K)
    Hermite coefficients ordered from low to high. If `y` was 2-D,
    the coefficients for the data in column k  of `y` are in column
    `k`.

[residuals, rank, singular_values, rcond] : list
    These values are only returned if ``full == True``

    - residuals -- sum of squared residuals of the least squares fit
    - rank -- the numerical rank of the scaled Vandermonde matrix
    - singular_values -- singular values of the scaled Vandermonde matrix
    - rcond -- value of `rcond`.

    For more details, see `numpy.linalg.lstsq`.

Warns
-----
RankWarning
    The rank of the coefficient matrix in the least-squares fit is
    deficient. The warning is only raised if ``full = False``.  The
    warnings can be turned off by

    >>> import warnings
    >>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

See Also
--------
numpy.polynomial.chebyshev.chebfit
numpy.polynomial.legendre.legfit
numpy.polynomial.polynomial.polyfit
numpy.polynomial.hermite.hermfit
numpy.polynomial.laguerre.lagfit
hermeval : Evaluates a Hermite series.
hermevander : pseudo Vandermonde matrix of Hermite series.
hermeweight : HermiteE weight function.
numpy.linalg.lstsq : Computes a least-squares fit from the matrix.
scipy.interpolate.UnivariateSpline : Computes spline fits.

Notes
-----
The solution is the coefficients of the HermiteE series `p` that
minimizes the sum of the weighted squared errors

.. math:: E = \sum_j w_j^2 * |y_j - p(x_j)|^2,

where the :math:`w_j` are the weights. This problem is solved by
setting up the (typically) overdetermined matrix equation

.. math:: V(x) * c = w * y,

where `V` is the pseudo Vandermonde matrix of `x`, the elements of `c`
are the coefficients to be solved for, and the elements of `y` are the
observed values.  This equation is then solved using the singular value
decomposition of `V`.

If some of the singular values of `V` are so small that they are
neglected, then a `~exceptions.RankWarning` will be issued. This means that
the coefficient values may be poorly determined. Using a lower order fit
will usually get rid of the warning.  The `rcond` parameter can also be
set to a value smaller than its default, but the resulting fit may be
spurious and have large contributions from roundoff error.

Fits using HermiteE series are probably most useful when the data can
be approximated by ``sqrt(w(x)) * p(x)``, where ``w(x)`` is the HermiteE
weight. In that case the weight ``sqrt(w(x[i]))`` should be used
together with data values ``y[i]/sqrt(w(x[i]))``. The weight function is
available as `hermeweight`.

References
----------
.. [1] Wikipedia, "Curve fitting",
       https://en.wikipedia.org/wiki/Curve_fitting

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite_e import hermefit, hermeval
>>> x = np.linspace(-10, 10)
>>> rng = np.random.default_rng()
>>> err = rng.normal(scale=1./10, size=len(x))
>>> y = hermeval(x, [1, 2, 3]) + err
>>> hermefit(x, y, 2)
array([1.02284196, 2.00032805, 2.99978457]) # may vary
- `hermediv` (ID: 91d2ebe6-1801-4eb2-8442-e1b74574230f): Divide one Hermite series by another.

Returns the quotient-with-remainder of two Hermite series
`c1` / `c2`.  The arguments are sequences of coefficients from lowest
order "term" to highest, e.g., [1,2,3] represents the series
``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
[quo, rem] : ndarrays
    Of Hermite series coefficients representing the quotient and
    remainder.

See Also
--------
hermeadd, hermesub, hermemulx, hermemul, hermepow

Notes
-----
In general, the (polynomial) division of one Hermite series by another
results in quotient and remainder terms that are not in the Hermite
polynomial basis set.  Thus, to express these results as a Hermite
series, it is necessary to "reproject" the results onto the Hermite
basis set, which may produce "unintuitive" (but correct) results; see
Examples section below.

Examples
--------
>>> from numpy.polynomial.hermite_e import hermediv
>>> hermediv([ 14.,  15.,  28.,   7.,   6.], [0, 1, 2])
(array([1., 2., 3.]), array([0.]))
>>> hermediv([ 15.,  17.,  28.,   7.,   6.], [0, 1, 2])
(array([1., 2., 3.]), array([1., 2.]))
- `hermeder` (ID: 2433a61e-ec6c-4862-8aa2-2c098c54493d): Differentiate a Hermite_e series.

Returns the series coefficients `c` differentiated `m` times along
`axis`.  At each iteration the result is multiplied by `scl` (the
scaling factor is for use in a linear change of variable). The argument
`c` is an array of coefficients from low to high degree along each
axis, e.g., [1,2,3] represents the series ``1*He_0 + 2*He_1 + 3*He_2``
while [[1,2],[1,2]] represents ``1*He_0(x)*He_0(y) + 1*He_1(x)*He_0(y)
+ 2*He_0(x)*He_1(y) + 2*He_1(x)*He_1(y)`` if axis=0 is ``x`` and axis=1
is ``y``.

Parameters
----------
c : array_like
    Array of Hermite_e series coefficients. If `c` is multidimensional
    the different axis correspond to different variables with the
    degree in each axis given by the corresponding index.
m : int, optional
    Number of derivatives taken, must be non-negative. (Default: 1)
scl : scalar, optional
    Each differentiation is multiplied by `scl`.  The end result is
    multiplication by ``scl**m``.  This is for use in a linear change of
    variable. (Default: 1)
axis : int, optional
    Axis over which the derivative is taken. (Default: 0).

Returns
-------
der : ndarray
    Hermite series of the derivative.

See Also
--------
hermeint

Notes
-----
In general, the result of differentiating a Hermite series does not
resemble the same operation on a power series. Thus the result of this
function may be "unintuitive," albeit correct; see Examples section
below.

Examples
--------
>>> from numpy.polynomial.hermite_e import hermeder
>>> hermeder([ 1.,  1.,  1.,  1.])
array([1.,  2.,  3.])
>>> hermeder([-0.25,  1.,  1./2.,  1./3.,  1./4 ], m=2)
array([1.,  2.,  3.])
- `hermecompanion` (ID: ba68838e-9b85-46c2-af13-62e954985a84): Return the scaled companion matrix of c.

The basis polynomials are scaled so that the companion matrix is
symmetric when `c` is an HermiteE basis polynomial. This provides
better eigenvalue estimates than the unscaled case and for basis
polynomials the eigenvalues are guaranteed to be real if
`numpy.linalg.eigvalsh` is used to obtain them.

Parameters
----------
c : array_like
    1-D array of HermiteE series coefficients ordered from low to high
    degree.

Returns
-------
mat : ndarray
    Scaled companion matrix of dimensions (deg, deg).
- `hermeadd` (ID: d9453f25-d088-44eb-b4f8-366cc602ee44): Add one Hermite series to another.

Returns the sum of two Hermite series `c1` + `c2`.  The arguments
are sequences of coefficients ordered from lowest order term to
highest, i.e., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the Hermite series of their sum.

See Also
--------
hermesub, hermemulx, hermemul, hermediv, hermepow

Notes
-----
Unlike multiplication, division, etc., the sum of two Hermite series
is a Hermite series (without having to "reproject" the result onto
the basis set) so addition, just like that of "standard" polynomials,
is simply "component-wise."

Examples
--------
>>> from numpy.polynomial.hermite_e import hermeadd
>>> hermeadd([1, 2, 3], [1, 2, 3, 4])
array([2.,  4.,  6.,  4.])
- `herme2poly` (ID: e84ce060-9d6a-4820-b74f-6b96281a51f4): Convert a Hermite series to a polynomial.

Convert an array representing the coefficients of a Hermite series,
ordered from lowest degree to highest, to an array of the coefficients
of the equivalent polynomial (relative to the "standard" basis) ordered
from lowest to highest degree.

Parameters
----------
c : array_like
    1-D array containing the Hermite series coefficients, ordered
    from lowest order term to highest.

Returns
-------
pol : ndarray
    1-D array containing the coefficients of the equivalent polynomial
    (relative to the "standard" basis) ordered from lowest order term
    to highest.

See Also
--------
poly2herme

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy.polynomial.hermite_e import herme2poly
>>> herme2poly([  2.,  10.,   2.,   3.])
array([0.,  1.,  2.,  3.])
- `poly2herm` (ID: 26cc2b97-c97c-45ac-8a79-39e0c2c8cb35): poly2herm(pol)

Convert a polynomial to a Hermite series.

Convert an array representing the coefficients of a polynomial (relative
to the "standard" basis) ordered from lowest degree to highest, to an
array of the coefficients of the equivalent Hermite series, ordered
from lowest to highest degree.

Parameters
----------
pol : array_like
    1-D array containing the polynomial coefficients

Returns
-------
c : ndarray
    1-D array containing the coefficients of the equivalent Hermite
    series.

See Also
--------
herm2poly

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy.polynomial.hermite import poly2herm
>>> poly2herm(np.arange(4))
array([1.   ,  2.75 ,  0.5  ,  0.375])
- `hermweight` (ID: 40f2968b-898b-453d-a650-8f7139d88dd5): Weight function of the Hermite polynomials.

The weight function is :math:`\exp(-x^2)` and the interval of
integration is :math:`[-\inf, \inf]`. the Hermite polynomials are
orthogonal, but not normalized, with respect to this weight function.

Parameters
----------
x : array_like
   Values at which the weight function will be computed.

Returns
-------
w : ndarray
   The weight function at `x`.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite import hermweight
>>> x = np.arange(-2, 2)
>>> hermweight(x)
array([0.01831564, 0.36787944, 1.        , 0.36787944])
- `hermvander3d` (ID: 84d6b443-5631-4d68-80e9-ec3dc0f07d44): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y, z)``. If `l`, `m`, `n` are the given degrees in `x`, `y`, `z`,
then The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (m+1)(n+1)i + (n+1)j + k] = H_i(x)*H_j(y)*H_k(z),

where ``0 <= i <= l``, ``0 <= j <= m``, and ``0 <= j <= n``.  The leading
indices of `V` index the points ``(x, y, z)`` and the last index encodes
the degrees of the Hermite polynomials.

If ``V = hermvander3d(x, y, z, [xdeg, ydeg, zdeg])``, then the columns
of `V` correspond to the elements of a 3-D coefficient array `c` of
shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

.. math:: c_{000}, c_{001}, c_{002},... , c_{010}, c_{011}, c_{012},...

and  ``np.dot(V, c.flat)`` and ``hermval3d(x, y, z, c)`` will be the
same up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 3-D Hermite
series of the same degrees and sample points.

Parameters
----------
x, y, z : array_like
    Arrays of point coordinates, all of the same shape. The dtypes will
    be converted to either float64 or complex128 depending on whether
    any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg, z_deg].

Returns
-------
vander3d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)*(deg[2]+1)`.  The dtype will
    be the same as the converted `x`, `y`, and `z`.

See Also
--------
hermvander, hermvander3d, hermval2d, hermval3d

Examples
--------
>>> from numpy.polynomial.hermite import hermvander3d
>>> x = np.array([-1, 0, 1])
>>> y = np.array([-1, 0, 1])
>>> z = np.array([-1, 0, 1])
>>> hermvander3d(x, y, z, [0, 1, 2])
array([[ 1., -2.,  2., -2.,  4., -4.],
       [ 1.,  0., -2.,  0.,  0., -0.],
       [ 1.,  2.,  2.,  2.,  4.,  4.]])
- `hermvander2d` (ID: 39d3ff12-7911-4496-82ba-2b6ccd83fd7a): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y)``. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (deg[1] + 1)*i + j] = H_i(x) * H_j(y),

where ``0 <= i <= deg[0]`` and ``0 <= j <= deg[1]``. The leading indices of
`V` index the points ``(x, y)`` and the last index encodes the degrees of
the Hermite polynomials.

If ``V = hermvander2d(x, y, [xdeg, ydeg])``, then the columns of `V`
correspond to the elements of a 2-D coefficient array `c` of shape
(xdeg + 1, ydeg + 1) in the order

.. math:: c_{00}, c_{01}, c_{02} ... , c_{10}, c_{11}, c_{12} ...

and ``np.dot(V, c.flat)`` and ``hermval2d(x, y, c)`` will be the same
up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 2-D Hermite
series of the same degrees and sample points.

Parameters
----------
x, y : array_like
    Arrays of point coordinates, all of the same shape. The dtypes
    will be converted to either float64 or complex128 depending on
    whether any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg].

Returns
-------
vander2d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)`.  The dtype will be the same
    as the converted `x` and `y`.

See Also
--------
hermvander, hermvander3d, hermval2d, hermval3d

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite import hermvander2d
>>> x = np.array([-1, 0, 1])
>>> y = np.array([-1, 0, 1])
>>> hermvander2d(x, y, [2, 2])
array([[ 1., -2.,  2., -2.,  4., -4.,  2., -4.,  4.],
       [ 1.,  0., -2.,  0.,  0., -0., -2., -0.,  4.],
       [ 1.,  2.,  2.,  2.,  4.,  4.,  2.,  4.,  4.]])
- `hermvander` (ID: 9dd43ccf-1005-490e-b347-e780c9c500cf): Pseudo-Vandermonde matrix of given degree.

Returns the pseudo-Vandermonde matrix of degree `deg` and sample points
`x`. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., i] = H_i(x),

where ``0 <= i <= deg``. The leading indices of `V` index the elements of
`x` and the last index is the degree of the Hermite polynomial.

If `c` is a 1-D array of coefficients of length ``n + 1`` and `V` is the
array ``V = hermvander(x, n)``, then ``np.dot(V, c)`` and
``hermval(x, c)`` are the same up to roundoff. This equivalence is
useful both for least squares fitting and for the evaluation of a large
number of Hermite series of the same degree and sample points.

Parameters
----------
x : array_like
    Array of points. The dtype is converted to float64 or complex128
    depending on whether any of the elements are complex. If `x` is
    scalar it is converted to a 1-D array.
deg : int
    Degree of the resulting matrix.

Returns
-------
vander : ndarray
    The pseudo-Vandermonde matrix. The shape of the returned matrix is
    ``x.shape + (deg + 1,)``, where The last index is the degree of the
    corresponding Hermite polynomial.  The dtype will be the same as
    the converted `x`.

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite import hermvander
>>> x = np.array([-1, 0, 1])
>>> hermvander(x, 3)
array([[ 1., -2.,  2.,  4.],
       [ 1.,  0., -2., -0.],
       [ 1.,  2.,  2., -4.]])
- `hermval3d` (ID: 4e4ff45e-0352-4768-b0d8-7bf679ea93bc): Evaluate a 3-D Hermite series at points (x, y, z).

This function returns the values:

.. math:: p(x,y,z) = \sum_{i,j,k} c_{i,j,k} * H_i(x) * H_j(y) * H_k(z)

The parameters `x`, `y`, and `z` are converted to arrays only if
they are tuples or a lists, otherwise they are treated as a scalars and
they must have the same shape after conversion. In either case, either
`x`, `y`, and `z` or their elements must support multiplication and
addition both with themselves and with the elements of `c`.

If `c` has fewer than 3 dimensions, ones are implicitly appended to its
shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape.

Parameters
----------
x, y, z : array_like, compatible object
    The three dimensional series is evaluated at the points
    ``(x, y, z)``, where `x`, `y`, and `z` must have the same shape.  If
    any of `x`, `y`, or `z` is a list or tuple, it is first converted
    to an ndarray, otherwise it is left unchanged and if it isn't an
    ndarray it is  treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j,k is contained in ``c[i,j,k]``. If `c` has dimension
    greater than 3 the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the multidimensional polynomial on points formed with
    triples of corresponding values from `x`, `y`, and `z`.

See Also
--------
hermval, hermval2d, hermgrid2d, hermgrid3d

Examples
--------
>>> from numpy.polynomial.hermite import hermval3d
>>> x = [1, 2]
>>> y = [4, 5]
>>> z = [6, 7]
>>> c = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
>>> hermval3d(x, y, z, c)
array([ 40077., 120131.])
- `hermval2d` (ID: b6529000-6c80-4e23-8b21-45dac5655468): Evaluate a 2-D Hermite series at points (x, y).

This function returns the values:

.. math:: p(x,y) = \sum_{i,j} c_{i,j} * H_i(x) * H_j(y)

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars and they
must have the same shape after conversion. In either case, either `x`
and `y` or their elements must support multiplication and addition both
with themselves and with the elements of `c`.

If `c` is a 1-D array a one is implicitly appended to its shape to make
it 2-D. The shape of the result will be c.shape[2:] + x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points ``(x, y)``,
    where `x` and `y` must have the same shape. If `x` or `y` is a list
    or tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and if it isn't an ndarray it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term
    of multi-degree i,j is contained in ``c[i,j]``. If `c` has
    dimension greater than two the remaining indices enumerate multiple
    sets of coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points formed with
    pairs of corresponding values from `x` and `y`.

See Also
--------
hermval, hermgrid2d, hermval3d, hermgrid3d

Examples
--------
>>> from numpy.polynomial.hermite import hermval2d
>>> x = [1, 2]
>>> y = [4, 5]
>>> c = [[1, 2, 3], [4, 5, 6]]
>>> hermval2d(x, y, c)
array([1035., 2883.])
- `hermval` (ID: 15986e67-a9d5-4057-b025-1300dbb1330a): Evaluate an Hermite series at points x.

If `c` is of length ``n + 1``, this function returns the value:

.. math:: p(x) = c_0 * H_0(x) + c_1 * H_1(x) + ... + c_n * H_n(x)

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `c`.

If `c` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If
`c` is multidimensional, then the shape of the result depends on the
value of `tensor`. If `tensor` is true the shape will be c.shape[1:] +
x.shape. If `tensor` is false the shape will be c.shape[1:]. Note that
scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so
they should be avoided if efficiency is a concern.

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    themselves and with the elements of `c`.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree n are contained in c[n]. If `c` is multidimensional the
    remaining indices enumerate multiple polynomials. In the two
    dimensional case the coefficients may be thought of as stored in
    the columns of `c`.
tensor : boolean, optional
    If True, the shape of the coefficient array is extended with ones
    on the right, one for each dimension of `x`. Scalars have dimension 0
    for this action. The result is that every column of coefficients in
    `c` is evaluated for every element of `x`. If False, `x` is broadcast
    over the columns of `c` for the evaluation.  This keyword is useful
    when `c` is multidimensional. The default value is True.

Returns
-------
values : ndarray, algebra_like
    The shape of the return value is described above.

See Also
--------
hermval2d, hermgrid2d, hermval3d, hermgrid3d

Notes
-----
The evaluation uses Clenshaw recursion, aka synthetic division.

Examples
--------
>>> from numpy.polynomial.hermite import hermval
>>> coef = [1,2,3]
>>> hermval(1, coef)
11.0
>>> hermval([[1,2],[3,4]], coef)
array([[ 11.,   51.],
       [115.,  203.]])
- `hermsub` (ID: aeb3d531-0ffd-4a1e-9c63-346c43683f5c): Subtract one Hermite series from another.

Returns the difference of two Hermite series `c1` - `c2`.  The
sequences of coefficients are from lowest order term to highest, i.e.,
[1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Hermite series coefficients representing their difference.

See Also
--------
hermadd, hermmulx, hermmul, hermdiv, hermpow

Notes
-----
Unlike multiplication, division, etc., the difference of two Hermite
series is a Hermite series (without having to "reproject" the result
onto the basis set) so subtraction, just like that of "standard"
polynomials, is simply "component-wise."

Examples
--------
>>> from numpy.polynomial.hermite import hermsub
>>> hermsub([1, 2, 3, 4], [1, 2, 3])
array([0.,  0.,  0.,  4.])
- `hermroots` (ID: 68ba0c84-0bda-4cdb-b603-fc1c293b6f07): Compute the roots of a Hermite series.

Return the roots (a.k.a. "zeros") of the polynomial

.. math:: p(x) = \sum_i c[i] * H_i(x).

Parameters
----------
c : 1-D array_like
    1-D array of coefficients.

Returns
-------
out : ndarray
    Array of the roots of the series. If all the roots are real,
    then `out` is also real, otherwise it is complex.

See Also
--------
numpy.polynomial.polynomial.polyroots
numpy.polynomial.legendre.legroots
numpy.polynomial.laguerre.lagroots
numpy.polynomial.chebyshev.chebroots
numpy.polynomial.hermite_e.hermeroots

Notes
-----
The root estimates are obtained as the eigenvalues of the companion
matrix, Roots far from the origin of the complex plane may have large
errors due to the numerical instability of the series for such
values. Roots with multiplicity greater than 1 will also show larger
errors as the value of the series near such points is relatively
insensitive to errors in the roots. Isolated roots near the origin can
be improved by a few iterations of Newton's method.

The Hermite series basis polynomials aren't powers of `x` so the
results of this function may seem unintuitive.

Examples
--------
>>> from numpy.polynomial.hermite import hermroots, hermfromroots
>>> coef = hermfromroots([-1, 0, 1])
>>> coef
array([0.   ,  0.25 ,  0.   ,  0.125])
>>> hermroots(coef)
array([-1.00000000e+00, -1.38777878e-17,  1.00000000e+00])
- `hermpow` (ID: ae59a39b-ddc6-47f9-8e4d-1b2318f1a347): Raise a Hermite series to a power.

Returns the Hermite series `c` raised to the power `pow`. The
argument `c` is a sequence of coefficients ordered from low to high.
i.e., [1,2,3] is the series  ``P_0 + 2*P_1 + 3*P_2.``

Parameters
----------
c : array_like
    1-D array of Hermite series coefficients ordered from low to
    high.
pow : integer
    Power to which the series will be raised
maxpower : integer, optional
    Maximum power allowed. This is mainly to limit growth of the series
    to unmanageable size. Default is 16

Returns
-------
coef : ndarray
    Hermite series of power.

See Also
--------
hermadd, hermsub, hermmulx, hermmul, hermdiv

Examples
--------
>>> from numpy.polynomial.hermite import hermpow
>>> hermpow([1, 2, 3], 2)
array([81.,  52.,  82.,  12.,   9.])
- `hermmulx` (ID: b1c21dbc-8578-46f3-88e6-4160490de099): Multiply a Hermite series by x.

Multiply the Hermite series `c` by x, where x is the independent
variable.


Parameters
----------
c : array_like
    1-D array of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the result of the multiplication.

See Also
--------
hermadd, hermsub, hermmul, hermdiv, hermpow

Notes
-----
The multiplication uses the recursion relationship for Hermite
polynomials in the form

.. math::

    xP_i(x) = (P_{i + 1}(x)/2 + i*P_{i - 1}(x))

Examples
--------
>>> from numpy.polynomial.hermite import hermmulx
>>> hermmulx([1, 2, 3])
array([2. , 6.5, 1. , 1.5])
- `hermmul` (ID: d094c586-f55d-4c94-95ce-a08c223e9bbb): Multiply one Hermite series by another.

Returns the product of two Hermite series `c1` * `c2`.  The arguments
are sequences of coefficients, from lowest order "term" to highest,
e.g., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Hermite series coefficients representing their product.

See Also
--------
hermadd, hermsub, hermmulx, hermdiv, hermpow

Notes
-----
In general, the (polynomial) product of two C-series results in terms
that are not in the Hermite polynomial basis set.  Thus, to express
the product as a Hermite series, it is necessary to "reproject" the
product onto said basis set, which may produce "unintuitive" (but
correct) results; see Examples section below.

Examples
--------
>>> from numpy.polynomial.hermite import hermmul
>>> hermmul([1, 2, 3], [0, 1, 2])
array([52.,  29.,  52.,   7.,   6.])
- `hermline` (ID: b8a9a858-b479-42d1-b732-ae4157ef803b): Hermite series whose graph is a straight line.



Parameters
----------
off, scl : scalars
    The specified line is given by ``off + scl*x``.

Returns
-------
y : ndarray
    This module's representation of the Hermite series for
    ``off + scl*x``.

See Also
--------
numpy.polynomial.polynomial.polyline
numpy.polynomial.chebyshev.chebline
numpy.polynomial.legendre.legline
numpy.polynomial.laguerre.lagline
numpy.polynomial.hermite_e.hermeline

Examples
--------
>>> from numpy.polynomial.hermite import hermline, hermval
>>> hermval(0,hermline(3, 2))
3.0
>>> hermval(1,hermline(3, 2))
5.0
- `hermint` (ID: 1399c5ef-9682-4423-bf4f-6c1f0c93174c): Integrate a Hermite series.

Returns the Hermite series coefficients `c` integrated `m` times from
`lbnd` along `axis`. At each iteration the resulting series is
**multiplied** by `scl` and an integration constant, `k`, is added.
The scaling factor is for use in a linear change of variable.  ("Buyer
beware": note that, depending on what one is doing, one may want `scl`
to be the reciprocal of what one might expect; for more information,
see the Notes section below.)  The argument `c` is an array of
coefficients from low to high degree along each axis, e.g., [1,2,3]
represents the series ``H_0 + 2*H_1 + 3*H_2`` while [[1,2],[1,2]]
represents ``1*H_0(x)*H_0(y) + 1*H_1(x)*H_0(y) + 2*H_0(x)*H_1(y) +
2*H_1(x)*H_1(y)`` if axis=0 is ``x`` and axis=1 is ``y``.

Parameters
----------
c : array_like
    Array of Hermite series coefficients. If c is multidimensional the
    different axis correspond to different variables with the degree in
    each axis given by the corresponding index.
m : int, optional
    Order of integration, must be positive. (Default: 1)
k : {[], list, scalar}, optional
    Integration constant(s).  The value of the first integral at
    ``lbnd`` is the first value in the list, the value of the second
    integral at ``lbnd`` is the second value, etc.  If ``k == []`` (the
    default), all constants are set to zero.  If ``m == 1``, a single
    scalar can be given instead of a list.
lbnd : scalar, optional
    The lower bound of the integral. (Default: 0)
scl : scalar, optional
    Following each integration the result is *multiplied* by `scl`
    before the integration constant is added. (Default: 1)
axis : int, optional
    Axis over which the integral is taken. (Default: 0).

Returns
-------
S : ndarray
    Hermite series coefficients of the integral.

Raises
------
ValueError
    If ``m < 0``, ``len(k) > m``, ``np.ndim(lbnd) != 0``, or
    ``np.ndim(scl) != 0``.

See Also
--------
hermder

Notes
-----
Note that the result of each integration is *multiplied* by `scl`.
Why is this important to note?  Say one is making a linear change of
variable :math:`u = ax + b` in an integral relative to `x`.  Then
:math:`dx = du/a`, so one will need to set `scl` equal to
:math:`1/a` - perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs
to be "reprojected" onto the C-series basis set.  Thus, typically,
the result of this function is "unintuitive," albeit correct; see
Examples section below.

Examples
--------
>>> from numpy.polynomial.hermite import hermint
>>> hermint([1,2,3]) # integrate once, value 0 at 0.
array([1. , 0.5, 0.5, 0.5])
>>> hermint([1,2,3], m=2) # integrate twice, value & deriv 0 at 0
array([-0.5       ,  0.5       ,  0.125     ,  0.08333333,  0.0625    ]) # may vary
>>> hermint([1,2,3], k=1) # integrate once, value 1 at 0.
array([2. , 0.5, 0.5, 0.5])
>>> hermint([1,2,3], lbnd=-1) # integrate once, value 0 at -1
array([-2. ,  0.5,  0.5,  0.5])
>>> hermint([1,2,3], m=2, k=[1,2], lbnd=-1)
array([ 1.66666667, -0.5       ,  0.125     ,  0.08333333,  0.0625    ]) # may vary
- `hermgrid3d` (ID: d48100a6-3922-4958-b48a-cb974d7fb023): Evaluate a 3-D Hermite series on the Cartesian product of x, y, and z.

This function returns the values:

.. math:: p(a,b,c) = \sum_{i,j,k} c_{i,j,k} * H_i(a) * H_j(b) * H_k(c)

where the points ``(a, b, c)`` consist of all triples formed by taking
`a` from `x`, `b` from `y`, and `c` from `z`. The resulting points form
a grid with `x` in the first dimension, `y` in the second, and `z` in
the third.

The parameters `x`, `y`, and `z` are converted to arrays only if they
are tuples or a lists, otherwise they are treated as a scalars. In
either case, either `x`, `y`, and `z` or their elements must support
multiplication and addition both with themselves and with the elements
of `c`.

If `c` has fewer than three dimensions, ones are implicitly appended to
its shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape + y.shape + z.shape.

Parameters
----------
x, y, z : array_like, compatible objects
    The three dimensional series is evaluated at the points in the
    Cartesian product of `x`, `y`, and `z`.  If `x`, `y`, or `z` is a
    list or tuple, it is first converted to an ndarray, otherwise it is
    left unchanged and, if it isn't an ndarray, it is treated as a
    scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
hermval, hermval2d, hermgrid2d, hermval3d

Examples
--------
>>> from numpy.polynomial.hermite import hermgrid3d
>>> x = [1, 2]
>>> y = [4, 5]
>>> z = [6, 7]
>>> c = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
>>> hermgrid3d(x, y, z, c)
array([[[ 40077.,  54117.],
        [ 49293.,  66561.]],
       [[ 72375.,  97719.],
        [ 88975., 120131.]]])
- `hermgrid2d` (ID: 140e6a04-0444-4af2-b37b-b281ab0dd787): Evaluate a 2-D Hermite series on the Cartesian product of x and y.

This function returns the values:

.. math:: p(a,b) = \sum_{i,j} c_{i,j} * H_i(a) * H_j(b)

where the points ``(a, b)`` consist of all pairs formed by taking
`a` from `x` and `b` from `y`. The resulting points form a grid with
`x` in the first dimension and `y` in the second.

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars. In either
case, either `x` and `y` or their elements must support multiplication
and addition both with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points in the
    Cartesian product of `x` and `y`.  If `x` or `y` is a list or
    tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
hermval, hermval2d, hermval3d, hermgrid3d

Examples
--------
>>> from numpy.polynomial.hermite import hermgrid2d
>>> x = [1, 2, 3]
>>> y = [4, 5]
>>> c = [[1, 2, 3], [4, 5, 6]]
>>> hermgrid2d(x, y, c)
array([[1035., 1599.],
       [1867., 2883.],
       [2699., 4167.]])
- `hermgauss` (ID: 8a4dd647-10a9-48ab-8f4d-6f5ef7f4f321): Gauss-Hermite quadrature.

Computes the sample points and weights for Gauss-Hermite quadrature.
These sample points and weights will correctly integrate polynomials of
degree :math:`2*deg - 1` or less over the interval :math:`[-\inf, \inf]`
with the weight function :math:`f(x) = \exp(-x^2)`.

Parameters
----------
deg : int
    Number of sample points and weights. It must be >= 1.

Returns
-------
x : ndarray
    1-D ndarray containing the sample points.
y : ndarray
    1-D ndarray containing the weights.

Notes
-----
The results have only been tested up to degree 100, higher degrees may
be problematic. The weights are determined by using the fact that

.. math:: w_k = c / (H'_n(x_k) * H_{n-1}(x_k))

where :math:`c` is a constant independent of :math:`k` and :math:`x_k`
is the k'th root of :math:`H_n`, and then scaling the results to get
the right value when integrating 1.

Examples
--------
>>> from numpy.polynomial.hermite import hermgauss
>>> hermgauss(2)
(array([-0.70710678,  0.70710678]), array([0.88622693, 0.88622693]))
- `hermfromroots` (ID: e974d2f7-4997-4761-b10e-93b91bec834b): Generate a Hermite series with given roots.

The function returns the coefficients of the polynomial

.. math:: p(x) = (x - r_0) * (x - r_1) * ... * (x - r_n),

in Hermite form, where the :math:`r_n` are the roots specified in `roots`.
If a zero has multiplicity n, then it must appear in `roots` n times.
For instance, if 2 is a root of multiplicity three and 3 is a root of
multiplicity 2, then `roots` looks something like [2, 2, 2, 3, 3]. The
roots can appear in any order.

If the returned coefficients are `c`, then

.. math:: p(x) = c_0 + c_1 * H_1(x) + ... +  c_n * H_n(x)

The coefficient of the last term is not generally 1 for monic
polynomials in Hermite form.

Parameters
----------
roots : array_like
    Sequence containing the roots.

Returns
-------
out : ndarray
    1-D array of coefficients.  If all roots are real then `out` is a
    real array, if some of the roots are complex, then `out` is complex
    even if all the coefficients in the result are real (see Examples
    below).

See Also
--------
numpy.polynomial.polynomial.polyfromroots
numpy.polynomial.legendre.legfromroots
numpy.polynomial.laguerre.lagfromroots
numpy.polynomial.chebyshev.chebfromroots
numpy.polynomial.hermite_e.hermefromroots

Examples
--------
>>> from numpy.polynomial.hermite import hermfromroots, hermval
>>> coef = hermfromroots((-1, 0, 1))
>>> hermval((-1, 0, 1), coef)
array([0.,  0.,  0.])
>>> coef = hermfromroots((-1j, 1j))
>>> hermval((-1j, 1j), coef)
array([0.+0.j, 0.+0.j])
- `hermfit` (ID: f7240a85-036d-4b94-a32a-fa694ad90100): Least squares fit of Hermite series to data.

Return the coefficients of a Hermite series of degree `deg` that is the
least squares fit to the data values `y` given at points `x`. If `y` is
1-D the returned coefficients will also be 1-D. If `y` is 2-D multiple
fits are done, one for each column of `y`, and the resulting
coefficients are stored in the corresponding columns of a 2-D return.
The fitted polynomial(s) are in the form

.. math::  p(x) = c_0 + c_1 * H_1(x) + ... + c_n * H_n(x),

where `n` is `deg`.

Parameters
----------
x : array_like, shape (M,)
    x-coordinates of the M sample points ``(x[i], y[i])``.
y : array_like, shape (M,) or (M, K)
    y-coordinates of the sample points. Several data sets of sample
    points sharing the same x-coordinates can be fitted at once by
    passing in a 2D-array that contains one dataset per column.
deg : int or 1-D array_like
    Degree(s) of the fitting polynomials. If `deg` is a single integer
    all terms up to and including the `deg`'th term are included in the
    fit. For NumPy versions >= 1.11.0 a list of integers specifying the
    degrees of the terms to include may be used instead.
rcond : float, optional
    Relative condition number of the fit. Singular values smaller than
    this relative to the largest singular value will be ignored. The
    default value is len(x)*eps, where eps is the relative precision of
    the float type, about 2e-16 in most cases.
full : bool, optional
    Switch determining nature of return value. When it is False (the
    default) just the coefficients are returned, when True diagnostic
    information from the singular value decomposition is also returned.
w : array_like, shape (`M`,), optional
    Weights. If not None, the weight ``w[i]`` applies to the unsquared
    residual ``y[i] - y_hat[i]`` at ``x[i]``. Ideally the weights are
    chosen so that the errors of the products ``w[i]*y[i]`` all have the
    same variance.  When using inverse-variance weighting, use
    ``w[i] = 1/sigma(y[i])``.  The default value is None.

Returns
-------
coef : ndarray, shape (M,) or (M, K)
    Hermite coefficients ordered from low to high. If `y` was 2-D,
    the coefficients for the data in column k  of `y` are in column
    `k`.

[residuals, rank, singular_values, rcond] : list
    These values are only returned if ``full == True``

    - residuals -- sum of squared residuals of the least squares fit
    - rank -- the numerical rank of the scaled Vandermonde matrix
    - singular_values -- singular values of the scaled Vandermonde matrix
    - rcond -- value of `rcond`.

    For more details, see `numpy.linalg.lstsq`.

Warns
-----
RankWarning
    The rank of the coefficient matrix in the least-squares fit is
    deficient. The warning is only raised if ``full == False``.  The
    warnings can be turned off by

    >>> import warnings
    >>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

See Also
--------
numpy.polynomial.chebyshev.chebfit
numpy.polynomial.legendre.legfit
numpy.polynomial.laguerre.lagfit
numpy.polynomial.polynomial.polyfit
numpy.polynomial.hermite_e.hermefit
hermval : Evaluates a Hermite series.
hermvander : Vandermonde matrix of Hermite series.
hermweight : Hermite weight function
numpy.linalg.lstsq : Computes a least-squares fit from the matrix.
scipy.interpolate.UnivariateSpline : Computes spline fits.

Notes
-----
The solution is the coefficients of the Hermite series `p` that
minimizes the sum of the weighted squared errors

.. math:: E = \sum_j w_j^2 * |y_j - p(x_j)|^2,

where the :math:`w_j` are the weights. This problem is solved by
setting up the (typically) overdetermined matrix equation

.. math:: V(x) * c = w * y,

where `V` is the weighted pseudo Vandermonde matrix of `x`, `c` are the
coefficients to be solved for, `w` are the weights, `y` are the
observed values.  This equation is then solved using the singular value
decomposition of `V`.

If some of the singular values of `V` are so small that they are
neglected, then a `~exceptions.RankWarning` will be issued. This means that
the coefficient values may be poorly determined. Using a lower order fit
will usually get rid of the warning.  The `rcond` parameter can also be
set to a value smaller than its default, but the resulting fit may be
spurious and have large contributions from roundoff error.

Fits using Hermite series are probably most useful when the data can be
approximated by ``sqrt(w(x)) * p(x)``, where ``w(x)`` is the Hermite
weight. In that case the weight ``sqrt(w(x[i]))`` should be used
together with data values ``y[i]/sqrt(w(x[i]))``. The weight function is
available as `hermweight`.

References
----------
.. [1] Wikipedia, "Curve fitting",
       https://en.wikipedia.org/wiki/Curve_fitting

Examples
--------
>>> import numpy as np
>>> from numpy.polynomial.hermite import hermfit, hermval
>>> x = np.linspace(-10, 10)
>>> rng = np.random.default_rng()
>>> err = rng.normal(scale=1./10, size=len(x))
>>> y = hermval(x, [1, 2, 3]) + err
>>> hermfit(x, y, 2)
array([1.02294967, 2.00016403, 2.99994614]) # may vary
- `hermdiv` (ID: b9f4ec7f-096e-48e5-aa1a-1f53f809e033): Divide one Hermite series by another.

Returns the quotient-with-remainder of two Hermite series
`c1` / `c2`.  The arguments are sequences of coefficients from lowest
order "term" to highest, e.g., [1,2,3] represents the series
``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
[quo, rem] : ndarrays
    Of Hermite series coefficients representing the quotient and
    remainder.

See Also
--------
hermadd, hermsub, hermmulx, hermmul, hermpow

Notes
-----
In general, the (polynomial) division of one Hermite series by another
results in quotient and remainder terms that are not in the Hermite
polynomial basis set.  Thus, to express these results as a Hermite
series, it is necessary to "reproject" the results onto the Hermite
basis set, which may produce "unintuitive" (but correct) results; see
Examples section below.

Examples
--------
>>> from numpy.polynomial.hermite import hermdiv
>>> hermdiv([ 52.,  29.,  52.,   7.,   6.], [0, 1, 2])
(array([1., 2., 3.]), array([0.]))
>>> hermdiv([ 54.,  31.,  52.,   7.,   6.], [0, 1, 2])
(array([1., 2., 3.]), array([2., 2.]))
>>> hermdiv([ 53.,  30.,  52.,   7.,   6.], [0, 1, 2])
(array([1., 2., 3.]), array([1., 1.]))
- `hermder` (ID: 16ecffa0-d532-4ee0-9106-55c5588ec779): Differentiate a Hermite series.

Returns the Hermite series coefficients `c` differentiated `m` times
along `axis`.  At each iteration the result is multiplied by `scl` (the
scaling factor is for use in a linear change of variable). The argument
`c` is an array of coefficients from low to high degree along each
axis, e.g., [1,2,3] represents the series ``1*H_0 + 2*H_1 + 3*H_2``
while [[1,2],[1,2]] represents ``1*H_0(x)*H_0(y) + 1*H_1(x)*H_0(y) +
2*H_0(x)*H_1(y) + 2*H_1(x)*H_1(y)`` if axis=0 is ``x`` and axis=1 is
``y``.

Parameters
----------
c : array_like
    Array of Hermite series coefficients. If `c` is multidimensional the
    different axis correspond to different variables with the degree in
    each axis given by the corresponding index.
m : int, optional
    Number of derivatives taken, must be non-negative. (Default: 1)
scl : scalar, optional
    Each differentiation is multiplied by `scl`.  The end result is
    multiplication by ``scl**m``.  This is for use in a linear change of
    variable. (Default: 1)
axis : int, optional
    Axis over which the derivative is taken. (Default: 0).

Returns
-------
der : ndarray
    Hermite series of the derivative.

See Also
--------
hermint

Notes
-----
In general, the result of differentiating a Hermite series does not
resemble the same operation on a power series. Thus the result of this
function may be "unintuitive," albeit correct; see Examples section
below.

Examples
--------
>>> from numpy.polynomial.hermite import hermder
>>> hermder([ 1. ,  0.5,  0.5,  0.5])
array([1., 2., 3.])
>>> hermder([-0.5,  1./2.,  1./8.,  1./12.,  1./16.], m=2)
array([1., 2., 3.])
- `hermcompanion` (ID: 568a94e3-708f-4f6d-9217-d516121c827c): Return the scaled companion matrix of c.

The basis polynomials are scaled so that the companion matrix is
symmetric when `c` is an Hermite basis polynomial. This provides
better eigenvalue estimates than the unscaled case and for basis
polynomials the eigenvalues are guaranteed to be real if
`numpy.linalg.eigvalsh` is used to obtain them.

Parameters
----------
c : array_like
    1-D array of Hermite series coefficients ordered from low to high
    degree.

Returns
-------
mat : ndarray
    Scaled companion matrix of dimensions (deg, deg).

Examples
--------
>>> from numpy.polynomial.hermite import hermcompanion
>>> hermcompanion([1, 0, 1])
array([[0.        , 0.35355339],
       [0.70710678, 0.        ]])
- `hermadd` (ID: 3ce797b1-18b4-4f91-b371-7294c6948353): Add one Hermite series to another.

Returns the sum of two Hermite series `c1` + `c2`.  The arguments
are sequences of coefficients ordered from lowest order term to
highest, i.e., [1,2,3] represents the series ``P_0 + 2*P_1 + 3*P_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Hermite series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the Hermite series of their sum.

See Also
--------
hermsub, hermmulx, hermmul, hermdiv, hermpow

Notes
-----
Unlike multiplication, division, etc., the sum of two Hermite series
is a Hermite series (without having to "reproject" the result onto
the basis set) so addition, just like that of "standard" polynomials,
is simply "component-wise."

Examples
--------
>>> from numpy.polynomial.hermite import hermadd
>>> hermadd([1, 2, 3], [1, 2, 3, 4])
array([2., 4., 6., 4.])
- `herm2poly` (ID: 99a99b50-1a55-424d-8148-6e9e9fe58262): Convert a Hermite series to a polynomial.

Convert an array representing the coefficients of a Hermite series,
ordered from lowest degree to highest, to an array of the coefficients
of the equivalent polynomial (relative to the "standard" basis) ordered
from lowest to highest degree.

Parameters
----------
c : array_like
    1-D array containing the Hermite series coefficients, ordered
    from lowest order term to highest.

Returns
-------
pol : ndarray
    1-D array containing the coefficients of the equivalent polynomial
    (relative to the "standard" basis) ordered from lowest order term
    to highest.

See Also
--------
poly2herm

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy.polynomial.hermite import herm2poly
>>> herm2poly([ 1.   ,  2.75 ,  0.5  ,  0.375])
array([0., 1., 2., 3.])
- `poly2cheb` (ID: f4febef4-3416-470e-be1b-b8fd745b30d0): Convert a polynomial to a Chebyshev series.

Convert an array representing the coefficients of a polynomial (relative
to the "standard" basis) ordered from lowest degree to highest, to an
array of the coefficients of the equivalent Chebyshev series, ordered
from lowest to highest degree.

Parameters
----------
pol : array_like
    1-D array containing the polynomial coefficients

Returns
-------
c : ndarray
    1-D array containing the coefficients of the equivalent Chebyshev
    series.

See Also
--------
cheb2poly

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy import polynomial as P
>>> p = P.Polynomial(range(4))
>>> p
Polynomial([0., 1., 2., 3.], domain=[-1.,  1.], window=[-1.,  1.], symbol='x')
>>> c = p.convert(kind=P.Chebyshev)
>>> c
Chebyshev([1.  , 3.25, 1.  , 0.75], domain=[-1.,  1.], window=[-1., ...
>>> P.chebyshev.poly2cheb(range(4))
array([1.  , 3.25, 1.  , 0.75])
- `chebweight` (ID: 81c0a3fb-e370-4200-93f7-685e67107507): The weight function of the Chebyshev polynomials.

The weight function is :math:`1/\sqrt{1 - x^2}` and the interval of
integration is :math:`[-1, 1]`. The Chebyshev polynomials are
orthogonal, but not normalized, with respect to this weight function.

Parameters
----------
x : array_like
   Values at which the weight function will be computed.

Returns
-------
w : ndarray
   The weight function at `x`.
- `chebvander3d` (ID: fe5d8be9-a23b-46ff-a343-640ed1f301a0): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y, z)``. If `l`, `m`, `n` are the given degrees in `x`, `y`, `z`,
then The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (m+1)(n+1)i + (n+1)j + k] = T_i(x)*T_j(y)*T_k(z),

where ``0 <= i <= l``, ``0 <= j <= m``, and ``0 <= j <= n``.  The leading
indices of `V` index the points ``(x, y, z)`` and the last index encodes
the degrees of the Chebyshev polynomials.

If ``V = chebvander3d(x, y, z, [xdeg, ydeg, zdeg])``, then the columns
of `V` correspond to the elements of a 3-D coefficient array `c` of
shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

.. math:: c_{000}, c_{001}, c_{002},... , c_{010}, c_{011}, c_{012},...

and ``np.dot(V, c.flat)`` and ``chebval3d(x, y, z, c)`` will be the
same up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 3-D Chebyshev
series of the same degrees and sample points.

Parameters
----------
x, y, z : array_like
    Arrays of point coordinates, all of the same shape. The dtypes will
    be converted to either float64 or complex128 depending on whether
    any of the elements are complex. Scalars are converted to 1-D
    arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg, z_deg].

Returns
-------
vander3d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)*(deg[2]+1)`.  The dtype will
    be the same as the converted `x`, `y`, and `z`.

See Also
--------
chebvander, chebvander3d, chebval2d, chebval3d
- `chebvander2d` (ID: 397215d6-8626-4632-bfb1-e101f7deee51): Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees `deg` and sample
points ``(x, y)``. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., (deg[1] + 1)*i + j] = T_i(x) * T_j(y),

where ``0 <= i <= deg[0]`` and ``0 <= j <= deg[1]``. The leading indices of
`V` index the points ``(x, y)`` and the last index encodes the degrees of
the Chebyshev polynomials.

If ``V = chebvander2d(x, y, [xdeg, ydeg])``, then the columns of `V`
correspond to the elements of a 2-D coefficient array `c` of shape
(xdeg + 1, ydeg + 1) in the order

.. math:: c_{00}, c_{01}, c_{02} ... , c_{10}, c_{11}, c_{12} ...

and ``np.dot(V, c.flat)`` and ``chebval2d(x, y, c)`` will be the same
up to roundoff. This equivalence is useful both for least squares
fitting and for the evaluation of a large number of 2-D Chebyshev
series of the same degrees and sample points.

Parameters
----------
x, y : array_like
    Arrays of point coordinates, all of the same shape. The dtypes
    will be converted to either float64 or complex128 depending on
    whether any of the elements are complex. Scalars are converted to
    1-D arrays.
deg : list of ints
    List of maximum degrees of the form [x_deg, y_deg].

Returns
-------
vander2d : ndarray
    The shape of the returned matrix is ``x.shape + (order,)``, where
    :math:`order = (deg[0]+1)*(deg[1]+1)`.  The dtype will be the same
    as the converted `x` and `y`.

See Also
--------
chebvander, chebvander3d, chebval2d, chebval3d
- `chebvander` (ID: 1349076c-3956-445a-a266-db74da5049b4): Pseudo-Vandermonde matrix of given degree.

Returns the pseudo-Vandermonde matrix of degree `deg` and sample points
`x`. The pseudo-Vandermonde matrix is defined by

.. math:: V[..., i] = T_i(x),

where ``0 <= i <= deg``. The leading indices of `V` index the elements of
`x` and the last index is the degree of the Chebyshev polynomial.

If `c` is a 1-D array of coefficients of length ``n + 1`` and `V` is the
matrix ``V = chebvander(x, n)``, then ``np.dot(V, c)`` and
``chebval(x, c)`` are the same up to roundoff.  This equivalence is
useful both for least squares fitting and for the evaluation of a large
number of Chebyshev series of the same degree and sample points.

Parameters
----------
x : array_like
    Array of points. The dtype is converted to float64 or complex128
    depending on whether any of the elements are complex. If `x` is
    scalar it is converted to a 1-D array.
deg : int
    Degree of the resulting matrix.

Returns
-------
vander : ndarray
    The pseudo Vandermonde matrix. The shape of the returned matrix is
    ``x.shape + (deg + 1,)``, where The last index is the degree of the
    corresponding Chebyshev polynomial.  The dtype will be the same as
    the converted `x`.
- `chebval3d` (ID: 5e47c27c-acd6-4378-8c53-0165e9e9aabc): Evaluate a 3-D Chebyshev series at points (x, y, z).

This function returns the values:

.. math:: p(x,y,z) = \sum_{i,j,k} c_{i,j,k} * T_i(x) * T_j(y) * T_k(z)

The parameters `x`, `y`, and `z` are converted to arrays only if
they are tuples or a lists, otherwise they are treated as a scalars and
they must have the same shape after conversion. In either case, either
`x`, `y`, and `z` or their elements must support multiplication and
addition both with themselves and with the elements of `c`.

If `c` has fewer than 3 dimensions, ones are implicitly appended to its
shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape.

Parameters
----------
x, y, z : array_like, compatible object
    The three dimensional series is evaluated at the points
    ``(x, y, z)``, where `x`, `y`, and `z` must have the same shape.  If
    any of `x`, `y`, or `z` is a list or tuple, it is first converted
    to an ndarray, otherwise it is left unchanged and if it isn't an
    ndarray it is  treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j,k is contained in ``c[i,j,k]``. If `c` has dimension
    greater than 3 the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the multidimensional polynomial on points formed with
    triples of corresponding values from `x`, `y`, and `z`.

See Also
--------
chebval, chebval2d, chebgrid2d, chebgrid3d
- `chebval2d` (ID: 479d63ba-691d-43ac-99b8-4802574702c0): Evaluate a 2-D Chebyshev series at points (x, y).

This function returns the values:

.. math:: p(x,y) = \sum_{i,j} c_{i,j} * T_i(x) * T_j(y)

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars and they
must have the same shape after conversion. In either case, either `x`
and `y` or their elements must support multiplication and addition both
with themselves and with the elements of `c`.

If `c` is a 1-D array a one is implicitly appended to its shape to make
it 2-D. The shape of the result will be c.shape[2:] + x.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points ``(x, y)``,
    where `x` and `y` must have the same shape. If `x` or `y` is a list
    or tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and if it isn't an ndarray it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term
    of multi-degree i,j is contained in ``c[i,j]``. If `c` has
    dimension greater than 2 the remaining indices enumerate multiple
    sets of coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional Chebyshev series at points formed
    from pairs of corresponding values from `x` and `y`.

See Also
--------
chebval, chebgrid2d, chebval3d, chebgrid3d
- `chebval` (ID: 44d5cfed-a6c4-454a-aec2-b3ab5b9b0c7b): Evaluate a Chebyshev series at points x.

If `c` is of length `n + 1`, this function returns the value:

.. math:: p(x) = c_0 * T_0(x) + c_1 * T_1(x) + ... + c_n * T_n(x)

The parameter `x` is converted to an array only if it is a tuple or a
list, otherwise it is treated as a scalar. In either case, either `x`
or its elements must support multiplication and addition both with
themselves and with the elements of `c`.

If `c` is a 1-D array, then ``p(x)`` will have the same shape as `x`.  If
`c` is multidimensional, then the shape of the result depends on the
value of `tensor`. If `tensor` is true the shape will be c.shape[1:] +
x.shape. If `tensor` is false the shape will be c.shape[1:]. Note that
scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so
they should be avoided if efficiency is a concern.

Parameters
----------
x : array_like, compatible object
    If `x` is a list or tuple, it is converted to an ndarray, otherwise
    it is left unchanged and treated as a scalar. In either case, `x`
    or its elements must support addition and multiplication with
    themselves and with the elements of `c`.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree n are contained in c[n]. If `c` is multidimensional the
    remaining indices enumerate multiple polynomials. In the two
    dimensional case the coefficients may be thought of as stored in
    the columns of `c`.
tensor : boolean, optional
    If True, the shape of the coefficient array is extended with ones
    on the right, one for each dimension of `x`. Scalars have dimension 0
    for this action. The result is that every column of coefficients in
    `c` is evaluated for every element of `x`. If False, `x` is broadcast
    over the columns of `c` for the evaluation.  This keyword is useful
    when `c` is multidimensional. The default value is True.

Returns
-------
values : ndarray, algebra_like
    The shape of the return value is described above.

See Also
--------
chebval2d, chebgrid2d, chebval3d, chebgrid3d

Notes
-----
The evaluation uses Clenshaw recursion, aka synthetic division.
- `chebsub` (ID: ef32bb4c-3584-4890-a3d0-34cb0820c620): Subtract one Chebyshev series from another.

Returns the difference of two Chebyshev series `c1` - `c2`.  The
sequences of coefficients are from lowest order term to highest, i.e.,
[1,2,3] represents the series ``T_0 + 2*T_1 + 3*T_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Chebyshev series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Chebyshev series coefficients representing their difference.

See Also
--------
chebadd, chebmulx, chebmul, chebdiv, chebpow

Notes
-----
Unlike multiplication, division, etc., the difference of two Chebyshev
series is a Chebyshev series (without having to "reproject" the result
onto the basis set) so subtraction, just like that of "standard"
polynomials, is simply "component-wise."

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> C.chebsub(c1,c2)
array([-2.,  0.,  2.])
>>> C.chebsub(c2,c1) # -C.chebsub(c1,c2)
array([ 2.,  0., -2.])
- `chebroots` (ID: 105be786-8a46-413f-82fb-dad3b808bbdb): Compute the roots of a Chebyshev series.

Return the roots (a.k.a. "zeros") of the polynomial

.. math:: p(x) = \sum_i c[i] * T_i(x).

Parameters
----------
c : 1-D array_like
    1-D array of coefficients.

Returns
-------
out : ndarray
    Array of the roots of the series. If all the roots are real,
    then `out` is also real, otherwise it is complex.

See Also
--------
numpy.polynomial.polynomial.polyroots
numpy.polynomial.legendre.legroots
numpy.polynomial.laguerre.lagroots
numpy.polynomial.hermite.hermroots
numpy.polynomial.hermite_e.hermeroots

Notes
-----
The root estimates are obtained as the eigenvalues of the companion
matrix, Roots far from the origin of the complex plane may have large
errors due to the numerical instability of the series for such
values. Roots with multiplicity greater than 1 will also show larger
errors as the value of the series near such points is relatively
insensitive to errors in the roots. Isolated roots near the origin can
be improved by a few iterations of Newton's method.

The Chebyshev series basis polynomials aren't powers of `x` so the
results of this function may seem unintuitive.

Examples
--------
>>> import numpy.polynomial.chebyshev as cheb
>>> cheb.chebroots((-1, 1,-1, 1)) # T3 - T2 + T1 - T0 has real roots
array([ -5.00000000e-01,   2.60860684e-17,   1.00000000e+00]) # may vary
- `chebpts2` (ID: 6f6477e4-fffc-4357-b2c4-472f8b5d251d): Chebyshev points of the second kind.

The Chebyshev points of the second kind are the points ``cos(x)``,
where ``x = [pi*k/(npts - 1) for k in range(npts)]`` sorted in ascending
order.

Parameters
----------
npts : int
    Number of sample points desired.

Returns
-------
pts : ndarray
    The Chebyshev points of the second kind.
- `chebpts1` (ID: 6da7f061-25bb-44e3-9a2f-784b0311bfda): Chebyshev points of the first kind.

The Chebyshev points of the first kind are the points ``cos(x)``,
where ``x = [pi*(k + .5)/npts for k in range(npts)]``.

Parameters
----------
npts : int
    Number of sample points desired.

Returns
-------
pts : ndarray
    The Chebyshev points of the first kind.

See Also
--------
chebpts2
- `chebpow` (ID: a127e364-b6e3-4f59-a62f-01052001c989): Raise a Chebyshev series to a power.

Returns the Chebyshev series `c` raised to the power `pow`. The
argument `c` is a sequence of coefficients ordered from low to high.
i.e., [1,2,3] is the series  ``T_0 + 2*T_1 + 3*T_2.``

Parameters
----------
c : array_like
    1-D array of Chebyshev series coefficients ordered from low to
    high.
pow : integer
    Power to which the series will be raised
maxpower : integer, optional
    Maximum power allowed. This is mainly to limit growth of the series
    to unmanageable size. Default is 16

Returns
-------
coef : ndarray
    Chebyshev series of power.

See Also
--------
chebadd, chebsub, chebmulx, chebmul, chebdiv

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> C.chebpow([1, 2, 3, 4], 2)
array([15.5, 22. , 16. , ..., 12.5, 12. ,  8. ])
- `chebmulx` (ID: b144d60a-c3ba-4666-9625-39c3f20a8c63): Multiply a Chebyshev series by x.

Multiply the polynomial `c` by x, where x is the independent
variable.


Parameters
----------
c : array_like
    1-D array of Chebyshev series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the result of the multiplication.

See Also
--------
chebadd, chebsub, chebmul, chebdiv, chebpow

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> C.chebmulx([1,2,3])
array([1. , 2.5, 1. , 1.5])
- `chebmul` (ID: aeef5db0-4ce9-4568-a430-12e8976c0644): Multiply one Chebyshev series by another.

Returns the product of two Chebyshev series `c1` * `c2`.  The arguments
are sequences of coefficients, from lowest order "term" to highest,
e.g., [1,2,3] represents the series ``T_0 + 2*T_1 + 3*T_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Chebyshev series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Of Chebyshev series coefficients representing their product.

See Also
--------
chebadd, chebsub, chebmulx, chebdiv, chebpow

Notes
-----
In general, the (polynomial) product of two C-series results in terms
that are not in the Chebyshev polynomial basis set.  Thus, to express
the product as a C-series, it is typically necessary to "reproject"
the product onto said basis set, which typically produces
"unintuitive live" (but correct) results; see Examples section below.

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> C.chebmul(c1,c2) # multiplication requires "reprojection"
array([  6.5,  12. ,  12. ,   4. ,   1.5])
- `chebline` (ID: 4a030d45-5b9b-48dc-b38a-d5cde35f5377): Chebyshev series whose graph is a straight line.

Parameters
----------
off, scl : scalars
    The specified line is given by ``off + scl*x``.

Returns
-------
y : ndarray
    This module's representation of the Chebyshev series for
    ``off + scl*x``.

See Also
--------
numpy.polynomial.polynomial.polyline
numpy.polynomial.legendre.legline
numpy.polynomial.laguerre.lagline
numpy.polynomial.hermite.hermline
numpy.polynomial.hermite_e.hermeline

Examples
--------
>>> import numpy.polynomial.chebyshev as C
>>> C.chebline(3,2)
array([3, 2])
>>> C.chebval(-3, C.chebline(3,2)) # should be -3
-3.0
- `chebinterpolate` (ID: 6cdc95cb-3807-41cf-bf71-01997cc854c7): Interpolate a function at the Chebyshev points of the first kind.

Returns the Chebyshev series that interpolates `func` at the Chebyshev
points of the first kind in the interval [-1, 1]. The interpolating
series tends to a minmax approximation to `func` with increasing `deg`
if the function is continuous in the interval.

Parameters
----------
func : function
    The function to be approximated. It must be a function of a single
    variable of the form ``f(x, a, b, c...)``, where ``a, b, c...`` are
    extra arguments passed in the `args` parameter.
deg : int
    Degree of the interpolating polynomial
args : tuple, optional
    Extra arguments to be used in the function call. Default is no extra
    arguments.

Returns
-------
coef : ndarray, shape (deg + 1,)
    Chebyshev coefficients of the interpolating series ordered from low to
    high.

Examples
--------
>>> import numpy.polynomial.chebyshev as C
>>> C.chebinterpolate(lambda x: np.tanh(x) + 0.5, 8)
array([  5.00000000e-01,   8.11675684e-01,  -9.86864911e-17,
        -5.42457905e-02,  -2.71387850e-16,   4.51658839e-03,
         2.46716228e-17,  -3.79694221e-04,  -3.26899002e-16])

Notes
-----
The Chebyshev polynomials used in the interpolation are orthogonal when
sampled at the Chebyshev points of the first kind. If it is desired to
constrain some of the coefficients they can simply be set to the desired
value after the interpolation, no new interpolation or fit is needed. This
is especially useful if it is known apriori that some of coefficients are
zero. For instance, if the function is even then the coefficients of the
terms of odd degree in the result can be set to zero.
- `chebint` (ID: 786a9162-3c9d-40d3-ba9f-ce067ab8fb37): Integrate a Chebyshev series.

Returns the Chebyshev series coefficients `c` integrated `m` times from
`lbnd` along `axis`. At each iteration the resulting series is
**multiplied** by `scl` and an integration constant, `k`, is added.
The scaling factor is for use in a linear change of variable.  ("Buyer
beware": note that, depending on what one is doing, one may want `scl`
to be the reciprocal of what one might expect; for more information,
see the Notes section below.)  The argument `c` is an array of
coefficients from low to high degree along each axis, e.g., [1,2,3]
represents the series ``T_0 + 2*T_1 + 3*T_2`` while [[1,2],[1,2]]
represents ``1*T_0(x)*T_0(y) + 1*T_1(x)*T_0(y) + 2*T_0(x)*T_1(y) +
2*T_1(x)*T_1(y)`` if axis=0 is ``x`` and axis=1 is ``y``.

Parameters
----------
c : array_like
    Array of Chebyshev series coefficients. If c is multidimensional
    the different axis correspond to different variables with the
    degree in each axis given by the corresponding index.
m : int, optional
    Order of integration, must be positive. (Default: 1)
k : {[], list, scalar}, optional
    Integration constant(s).  The value of the first integral at zero
    is the first value in the list, the value of the second integral
    at zero is the second value, etc.  If ``k == []`` (the default),
    all constants are set to zero.  If ``m == 1``, a single scalar can
    be given instead of a list.
lbnd : scalar, optional
    The lower bound of the integral. (Default: 0)
scl : scalar, optional
    Following each integration the result is *multiplied* by `scl`
    before the integration constant is added. (Default: 1)
axis : int, optional
    Axis over which the integral is taken. (Default: 0).

Returns
-------
S : ndarray
    C-series coefficients of the integral.

Raises
------
ValueError
    If ``m < 1``, ``len(k) > m``, ``np.ndim(lbnd) != 0``, or
    ``np.ndim(scl) != 0``.

See Also
--------
chebder

Notes
-----
Note that the result of each integration is *multiplied* by `scl`.
Why is this important to note?  Say one is making a linear change of
variable :math:`u = ax + b` in an integral relative to `x`.  Then
:math:`dx = du/a`, so one will need to set `scl` equal to
:math:`1/a`- perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs
to be "reprojected" onto the C-series basis set.  Thus, typically,
the result of this function is "unintuitive," albeit correct; see
Examples section below.

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> c = (1,2,3)
>>> C.chebint(c)
array([ 0.5, -0.5,  0.5,  0.5])
>>> C.chebint(c,3)
array([ 0.03125   , -0.1875    ,  0.04166667, -0.05208333,  0.01041667, # may vary
    0.00625   ])
>>> C.chebint(c, k=3)
array([ 3.5, -0.5,  0.5,  0.5])
>>> C.chebint(c,lbnd=-2)
array([ 8.5, -0.5,  0.5,  0.5])
>>> C.chebint(c,scl=-2)
array([-1.,  1., -1., -1.])
- `chebgrid3d` (ID: 6acef1c7-3326-4cec-9f6b-94891eb2be38): Evaluate a 3-D Chebyshev series on the Cartesian product of x, y, and z.

This function returns the values:

.. math:: p(a,b,c) = \sum_{i,j,k} c_{i,j,k} * T_i(a) * T_j(b) * T_k(c)

where the points ``(a, b, c)`` consist of all triples formed by taking
`a` from `x`, `b` from `y`, and `c` from `z`. The resulting points form
a grid with `x` in the first dimension, `y` in the second, and `z` in
the third.

The parameters `x`, `y`, and `z` are converted to arrays only if they
are tuples or a lists, otherwise they are treated as a scalars. In
either case, either `x`, `y`, and `z` or their elements must support
multiplication and addition both with themselves and with the elements
of `c`.

If `c` has fewer than three dimensions, ones are implicitly appended to
its shape to make it 3-D. The shape of the result will be c.shape[3:] +
x.shape + y.shape + z.shape.

Parameters
----------
x, y, z : array_like, compatible objects
    The three dimensional series is evaluated at the points in the
    Cartesian product of `x`, `y`, and `z`.  If `x`, `y`, or `z` is a
    list or tuple, it is first converted to an ndarray, otherwise it is
    left unchanged and, if it isn't an ndarray, it is treated as a
    scalar.
c : array_like
    Array of coefficients ordered so that the coefficients for terms of
    degree i,j are contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional polynomial at points in the Cartesian
    product of `x` and `y`.

See Also
--------
chebval, chebval2d, chebgrid2d, chebval3d
- `chebgrid2d` (ID: 602e8a49-7c57-4f44-a6d2-b914a1c01ccb): Evaluate a 2-D Chebyshev series on the Cartesian product of x and y.

This function returns the values:

.. math:: p(a,b) = \sum_{i,j} c_{i,j} * T_i(a) * T_j(b),

where the points `(a, b)` consist of all pairs formed by taking
`a` from `x` and `b` from `y`. The resulting points form a grid with
`x` in the first dimension and `y` in the second.

The parameters `x` and `y` are converted to arrays only if they are
tuples or a lists, otherwise they are treated as a scalars. In either
case, either `x` and `y` or their elements must support multiplication
and addition both with themselves and with the elements of `c`.

If `c` has fewer than two dimensions, ones are implicitly appended to
its shape to make it 2-D. The shape of the result will be c.shape[2:] +
x.shape + y.shape.

Parameters
----------
x, y : array_like, compatible objects
    The two dimensional series is evaluated at the points in the
    Cartesian product of `x` and `y`.  If `x` or `y` is a list or
    tuple, it is first converted to an ndarray, otherwise it is left
    unchanged and, if it isn't an ndarray, it is treated as a scalar.
c : array_like
    Array of coefficients ordered so that the coefficient of the term of
    multi-degree i,j is contained in ``c[i,j]``. If `c` has dimension
    greater than two the remaining indices enumerate multiple sets of
    coefficients.

Returns
-------
values : ndarray, compatible object
    The values of the two dimensional Chebyshev series at points in the
    Cartesian product of `x` and `y`.

See Also
--------
chebval, chebval2d, chebval3d, chebgrid3d
- `chebgauss` (ID: 2a40721a-7632-4134-ba58-33a2666ed6c8): Gauss-Chebyshev quadrature.

Computes the sample points and weights for Gauss-Chebyshev quadrature.
These sample points and weights will correctly integrate polynomials of
degree :math:`2*deg - 1` or less over the interval :math:`[-1, 1]` with
the weight function :math:`f(x) = 1/\sqrt{1 - x^2}`.

Parameters
----------
deg : int
    Number of sample points and weights. It must be >= 1.

Returns
-------
x : ndarray
    1-D ndarray containing the sample points.
y : ndarray
    1-D ndarray containing the weights.

Notes
-----
The results have only been tested up to degree 100, higher degrees may
be problematic. For Gauss-Chebyshev there are closed form solutions for
the sample points and weights. If n = `deg`, then

.. math:: x_i = \cos(\pi (2 i - 1) / (2 n))

.. math:: w_i = \pi / n
- `chebfromroots` (ID: d9ba3483-ae3c-4259-b515-ee729278099d): Generate a Chebyshev series with given roots.

The function returns the coefficients of the polynomial

.. math:: p(x) = (x - r_0) * (x - r_1) * ... * (x - r_n),

in Chebyshev form, where the :math:`r_n` are the roots specified in
`roots`.  If a zero has multiplicity n, then it must appear in `roots`
n times.  For instance, if 2 is a root of multiplicity three and 3 is a
root of multiplicity 2, then `roots` looks something like [2, 2, 2, 3, 3].
The roots can appear in any order.

If the returned coefficients are `c`, then

.. math:: p(x) = c_0 + c_1 * T_1(x) + ... +  c_n * T_n(x)

The coefficient of the last term is not generally 1 for monic
polynomials in Chebyshev form.

Parameters
----------
roots : array_like
    Sequence containing the roots.

Returns
-------
out : ndarray
    1-D array of coefficients.  If all roots are real then `out` is a
    real array, if some of the roots are complex, then `out` is complex
    even if all the coefficients in the result are real (see Examples
    below).

See Also
--------
numpy.polynomial.polynomial.polyfromroots
numpy.polynomial.legendre.legfromroots
numpy.polynomial.laguerre.lagfromroots
numpy.polynomial.hermite.hermfromroots
numpy.polynomial.hermite_e.hermefromroots

Examples
--------
>>> import numpy.polynomial.chebyshev as C
>>> C.chebfromroots((-1,0,1)) # x^3 - x relative to the standard basis
array([ 0.  , -0.25,  0.  ,  0.25])
>>> j = complex(0,1)
>>> C.chebfromroots((-j,j)) # x^2 + 1 relative to the standard basis
array([1.5+0.j, 0. +0.j, 0.5+0.j])
- `chebfit` (ID: 940caec9-c2a9-45e8-819e-bd9b645e208a): Least squares fit of Chebyshev series to data.

Return the coefficients of a Chebyshev series of degree `deg` that is the
least squares fit to the data values `y` given at points `x`. If `y` is
1-D the returned coefficients will also be 1-D. If `y` is 2-D multiple
fits are done, one for each column of `y`, and the resulting
coefficients are stored in the corresponding columns of a 2-D return.
The fitted polynomial(s) are in the form

.. math::  p(x) = c_0 + c_1 * T_1(x) + ... + c_n * T_n(x),

where `n` is `deg`.

Parameters
----------
x : array_like, shape (M,)
    x-coordinates of the M sample points ``(x[i], y[i])``.
y : array_like, shape (M,) or (M, K)
    y-coordinates of the sample points. Several data sets of sample
    points sharing the same x-coordinates can be fitted at once by
    passing in a 2D-array that contains one dataset per column.
deg : int or 1-D array_like
    Degree(s) of the fitting polynomials. If `deg` is a single integer,
    all terms up to and including the `deg`'th term are included in the
    fit. For NumPy versions >= 1.11.0 a list of integers specifying the
    degrees of the terms to include may be used instead.
rcond : float, optional
    Relative condition number of the fit. Singular values smaller than
    this relative to the largest singular value will be ignored. The
    default value is ``len(x)*eps``, where eps is the relative precision of
    the float type, about 2e-16 in most cases.
full : bool, optional
    Switch determining nature of return value. When it is False (the
    default) just the coefficients are returned, when True diagnostic
    information from the singular value decomposition is also returned.
w : array_like, shape (`M`,), optional
    Weights. If not None, the weight ``w[i]`` applies to the unsquared
    residual ``y[i] - y_hat[i]`` at ``x[i]``. Ideally the weights are
    chosen so that the errors of the products ``w[i]*y[i]`` all have the
    same variance.  When using inverse-variance weighting, use
    ``w[i] = 1/sigma(y[i])``.  The default value is None.

Returns
-------
coef : ndarray, shape (M,) or (M, K)
    Chebyshev coefficients ordered from low to high. If `y` was 2-D,
    the coefficients for the data in column k  of `y` are in column
    `k`.

[residuals, rank, singular_values, rcond] : list
    These values are only returned if ``full == True``

    - residuals -- sum of squared residuals of the least squares fit
    - rank -- the numerical rank of the scaled Vandermonde matrix
    - singular_values -- singular values of the scaled Vandermonde matrix
    - rcond -- value of `rcond`.

    For more details, see `numpy.linalg.lstsq`.

Warns
-----
RankWarning
    The rank of the coefficient matrix in the least-squares fit is
    deficient. The warning is only raised if ``full == False``.  The
    warnings can be turned off by

    >>> import warnings
    >>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

See Also
--------
numpy.polynomial.polynomial.polyfit
numpy.polynomial.legendre.legfit
numpy.polynomial.laguerre.lagfit
numpy.polynomial.hermite.hermfit
numpy.polynomial.hermite_e.hermefit
chebval : Evaluates a Chebyshev series.
chebvander : Vandermonde matrix of Chebyshev series.
chebweight : Chebyshev weight function.
numpy.linalg.lstsq : Computes a least-squares fit from the matrix.
scipy.interpolate.UnivariateSpline : Computes spline fits.

Notes
-----
The solution is the coefficients of the Chebyshev series `p` that
minimizes the sum of the weighted squared errors

.. math:: E = \sum_j w_j^2 * |y_j - p(x_j)|^2,

where :math:`w_j` are the weights. This problem is solved by setting up
as the (typically) overdetermined matrix equation

.. math:: V(x) * c = w * y,

where `V` is the weighted pseudo Vandermonde matrix of `x`, `c` are the
coefficients to be solved for, `w` are the weights, and `y` are the
observed values.  This equation is then solved using the singular value
decomposition of `V`.

If some of the singular values of `V` are so small that they are
neglected, then a `~exceptions.RankWarning` will be issued. This means that
the coefficient values may be poorly determined. Using a lower order fit
will usually get rid of the warning.  The `rcond` parameter can also be
set to a value smaller than its default, but the resulting fit may be
spurious and have large contributions from roundoff error.

Fits using Chebyshev series are usually better conditioned than fits
using power series, but much can depend on the distribution of the
sample points and the smoothness of the data. If the quality of the fit
is inadequate splines may be a good alternative.

References
----------
.. [1] Wikipedia, "Curve fitting",
       https://en.wikipedia.org/wiki/Curve_fitting

Examples
--------
- `chebdiv` (ID: b559ac42-e5ad-4d08-8ae8-d076b919603c): Divide one Chebyshev series by another.

Returns the quotient-with-remainder of two Chebyshev series
`c1` / `c2`.  The arguments are sequences of coefficients from lowest
order "term" to highest, e.g., [1,2,3] represents the series
``T_0 + 2*T_1 + 3*T_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Chebyshev series coefficients ordered from low to
    high.

Returns
-------
[quo, rem] : ndarrays
    Of Chebyshev series coefficients representing the quotient and
    remainder.

See Also
--------
chebadd, chebsub, chebmulx, chebmul, chebpow

Notes
-----
In general, the (polynomial) division of one C-series by another
results in quotient and remainder terms that are not in the Chebyshev
polynomial basis set.  Thus, to express these results as C-series, it
is typically necessary to "reproject" the results onto said basis
set, which typically produces "unintuitive" (but correct) results;
see Examples section below.

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> C.chebdiv(c1,c2) # quotient "intuitive," remainder not
(array([3.]), array([-8., -4.]))
>>> c2 = (0,1,2,3)
>>> C.chebdiv(c2,c1) # neither "intuitive"
(array([0., 2.]), array([-2., -4.]))
- `chebder` (ID: 0557529d-c29f-480f-a2b3-001486182f4d): Differentiate a Chebyshev series.

Returns the Chebyshev series coefficients `c` differentiated `m` times
along `axis`.  At each iteration the result is multiplied by `scl` (the
scaling factor is for use in a linear change of variable). The argument
`c` is an array of coefficients from low to high degree along each
axis, e.g., [1,2,3] represents the series ``1*T_0 + 2*T_1 + 3*T_2``
while [[1,2],[1,2]] represents ``1*T_0(x)*T_0(y) + 1*T_1(x)*T_0(y) +
2*T_0(x)*T_1(y) + 2*T_1(x)*T_1(y)`` if axis=0 is ``x`` and axis=1 is
``y``.

Parameters
----------
c : array_like
    Array of Chebyshev series coefficients. If c is multidimensional
    the different axis correspond to different variables with the
    degree in each axis given by the corresponding index.
m : int, optional
    Number of derivatives taken, must be non-negative. (Default: 1)
scl : scalar, optional
    Each differentiation is multiplied by `scl`.  The end result is
    multiplication by ``scl**m``.  This is for use in a linear change of
    variable. (Default: 1)
axis : int, optional
    Axis over which the derivative is taken. (Default: 0).

Returns
-------
der : ndarray
    Chebyshev series of the derivative.

See Also
--------
chebint

Notes
-----
In general, the result of differentiating a C-series needs to be
"reprojected" onto the C-series basis set. Thus, typically, the
result of this function is "unintuitive," albeit correct; see Examples
section below.

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> c = (1,2,3,4)
>>> C.chebder(c)
array([14., 12., 24.])
>>> C.chebder(c,3)
array([96.])
>>> C.chebder(c,scl=-1)
array([-14., -12., -24.])
>>> C.chebder(c,2,-1)
array([12.,  96.])
- `chebcompanion` (ID: 18151004-edd9-4051-aad0-4de1ada544b3): Return the scaled companion matrix of c.

The basis polynomials are scaled so that the companion matrix is
symmetric when `c` is a Chebyshev basis polynomial. This provides
better eigenvalue estimates than the unscaled case and for basis
polynomials the eigenvalues are guaranteed to be real if
`numpy.linalg.eigvalsh` is used to obtain them.

Parameters
----------
c : array_like
    1-D array of Chebyshev series coefficients ordered from low to high
    degree.

Returns
-------
mat : ndarray
    Scaled companion matrix of dimensions (deg, deg).
- `chebadd` (ID: cf8fd565-2c65-4010-a7cf-113611439438): Add one Chebyshev series to another.

Returns the sum of two Chebyshev series `c1` + `c2`.  The arguments
are sequences of coefficients ordered from lowest order term to
highest, i.e., [1,2,3] represents the series ``T_0 + 2*T_1 + 3*T_2``.

Parameters
----------
c1, c2 : array_like
    1-D arrays of Chebyshev series coefficients ordered from low to
    high.

Returns
-------
out : ndarray
    Array representing the Chebyshev series of their sum.

See Also
--------
chebsub, chebmulx, chebmul, chebdiv, chebpow

Notes
-----
Unlike multiplication, division, etc., the sum of two Chebyshev series
is a Chebyshev series (without having to "reproject" the result onto
the basis set) so addition, just like that of "standard" polynomials,
is simply "component-wise."

Examples
--------
>>> from numpy.polynomial import chebyshev as C
>>> c1 = (1,2,3)
>>> c2 = (3,2,1)
>>> C.chebadd(c1,c2)
array([4., 4., 4.])
- `cheb2poly` (ID: b1868ae5-81e6-4b9c-b6de-24b77acaf774): Convert a Chebyshev series to a polynomial.

Convert an array representing the coefficients of a Chebyshev series,
ordered from lowest degree to highest, to an array of the coefficients
of the equivalent polynomial (relative to the "standard" basis) ordered
from lowest to highest degree.

Parameters
----------
c : array_like
    1-D array containing the Chebyshev series coefficients, ordered
    from lowest order term to highest.

Returns
-------
pol : ndarray
    1-D array containing the coefficients of the equivalent polynomial
    (relative to the "standard" basis) ordered from lowest order term
    to highest.

See Also
--------
poly2cheb

Notes
-----
The easy way to do conversions between polynomial basis sets
is to use the convert method of a class instance.

Examples
--------
>>> from numpy import polynomial as P
>>> c = P.Chebyshev(range(4))
>>> c
Chebyshev([0., 1., 2., 3.], domain=[-1.,  1.], window=[-1.,  1.], symbol='x')
>>> p = c.convert(kind=P.Polynomial)
>>> p
Polynomial([-2., -8.,  4., 12.], domain=[-1.,  1.], window=[-1.,  1.], ...
>>> P.chebyshev.cheb2poly(range(4))
array([-2.,  -8.,   4.,  12.])
- `test_diagonal` (ID: 9ef28f1b-232f-4034-959c-f1edb49fb1be): No description
- `test_stack` (ID: a4bd4da2-83eb-4416-8ea8-5e07281637c4): No description
- `test_sort_matrix_none` (ID: dc32dbbc-889c-4c98-93db-9c8dfbbc1ce5): No description
- `test_polynomial_mapdomain` (ID: 4f23bc94-1ee3-4d5f-8dfe-fc07c2e82d42): No description
- `test_partition_matrix_none` (ID: f9bf2572-fcee-4a1d-9e3a-27d9dc3a2b16): No description
- `test_object_scalar_multiply` (ID: a867e9b5-9609-4b51-9dcf-1b1827d1fd41): No description
- `test_nanfunctions_matrices_general` (ID: 3bdbe443-dbb5-4b63-a3f9-d590fa5714e9): No description
- `test_nanfunctions_matrices` (ID: da82847c-81d8-4a00-b6a2-336c428b3469): No description
- `test_kron_matrix` (ID: a003b39f-930c-4592-b7fa-22a933d88bb3): No description
- `test_iter_allocate_output_subtype` (ID: 9de3a58f-aea0-4267-ac01-241e3a469abe): No description
- `test_inner_scalar_and_matrix_of_objects` (ID: d56f6f1a-fc54-416a-a3b0-b6842b41adc0): No description
- `test_inner_scalar_and_matrix` (ID: 604c8f31-534d-4458-a602-a978ca37c56a): No description
- `test_fancy_indexing` (ID: cd5b9d26-8458-45b9-9aad-0a688d4158e9): No description
- `test_ediff1d_matrix` (ID: eb88bda9-1a32-4ce4-8643-acfc1b591f49): No description
- `test_dot_scalar_and_matrix_of_objects` (ID: b83642db-e62d-45ba-91f2-ac2aa3ef1cb1): No description
- `test_dot_matrix` (ID: 40ec6a5c-232a-499a-8fd1-2fc2dfdd2f85): No description
- `test_average_matrix` (ID: 1a5b9616-513f-4f10-a995-5a6cdd54a05f): No description
- `test_array_equal_error_message_matrix` (ID: b55fe3be-552f-4fc1-8f64-a676eecbc2f4): No description
- `test_array_astype` (ID: 4b0588c0-db5a-45f8-a9d7-ec7eb76ab53b): No description
- `test_array_almost_equal_matrix` (ID: 98bdf1a7-0241-4074-bcf6-4d0d05a87b6f): No description
- `test_apply_along_axis_matrix` (ID: 7705d873-b113-434f-9adb-2c13e857d5c4): No description
- `like_function` (ID: 6413bad9-a663-487b-9c00-56ad8975ba77): No description
- `bmat` (ID: 8b25109d-3108-4118-9027-9159f2207590): Build a matrix object from a string, nested sequence, or array.

Parameters
----------
obj : str or array_like
    Input data. If a string, variables in the current scope may be
    referenced by name.
ldict : dict, optional
    A dictionary that replaces local operands in current frame.
    Ignored if `obj` is not a string or `gdict` is None.
gdict : dict, optional
    A dictionary that replaces global operands in current frame.
    Ignored if `obj` is not a string.

Returns
-------
out : matrix
    Returns a matrix object, which is a specialized 2-D array.

See Also
--------
block :
    A generalization of this function for N-d arrays, that returns normal
    ndarrays.

Examples
--------
>>> import numpy as np
>>> A = np.asmatrix('1 1; 1 1')
>>> B = np.asmatrix('2 2; 2 2')
>>> C = np.asmatrix('3 4; 5 6')
>>> D = np.asmatrix('7 8; 9 0')

All the following expressions construct the same block matrix:

>>> np.bmat([[A, B], [C, D]])
matrix([[1, 1, 2, 2],
        [1, 1, 2, 2],
        [3, 4, 7, 8],
        [5, 6, 9, 0]])
>>> np.bmat(np.r_[np.c_[A, B], np.c_[C, D]])
matrix([[1, 1, 2, 2],
        [1, 1, 2, 2],
        [3, 4, 7, 8],
        [5, 6, 9, 0]])
>>> np.bmat('A,B; C,D')
matrix([[1, 1, 2, 2],
        [1, 1, 2, 2],
        [3, 4, 7, 8],
        [5, 6, 9, 0]])
- `asmatrix` (ID: 7898450e-fee7-4a55-8c79-3c4eaaae0374): Interpret the input as a matrix.

Unlike `matrix`, `asmatrix` does not make a copy if the input is already
a matrix or an ndarray.  Equivalent to ``matrix(data, copy=False)``.

Parameters
----------
data : array_like
    Input data.
dtype : data-type
   Data-type of the output matrix.

Returns
-------
mat : matrix
    `data` interpreted as a matrix.

Examples
--------
>>> import numpy as np
>>> x = np.array([[1, 2], [3, 4]])

>>> m = np.asmatrix(x)

>>> x[0,0] = 5

>>> m
matrix([[5, 2],
        [3, 4]])
- `zeros` (ID: fbd0e487-a794-430a-8672-2c2e55cf84ce): Return a matrix of given shape and type, filled with zeros.

Parameters
----------
shape : int or sequence of ints
    Shape of the matrix
dtype : data-type, optional
    The desired data-type for the matrix, default is float.
order : {'C', 'F'}, optional
    Whether to store the result in C- or Fortran-contiguous order,
    default is 'C'.

Returns
-------
out : matrix
    Zero matrix of given shape, dtype, and order.

See Also
--------
numpy.zeros : Equivalent array function.
matlib.ones : Return a matrix of ones.

Notes
-----
If `shape` has length one i.e. ``(N,)``, or is a scalar ``N``,
`out` becomes a single row matrix of shape ``(1,N)``.

Examples
--------
>>> import numpy.matlib
>>> np.matlib.zeros((2, 3))
matrix([[0.,  0.,  0.],
        [0.,  0.,  0.]])

>>> np.matlib.zeros(2)
matrix([[0.,  0.]])
- `repmat` (ID: 2201fb09-4feb-4b38-8048-1b863212f188): Repeat a 0-D to 2-D array or matrix MxN times.

Parameters
----------
a : array_like
    The array or matrix to be repeated.
m, n : int
    The number of times `a` is repeated along the first and second axes.

Returns
-------
out : ndarray
    The result of repeating `a`.

Examples
--------
>>> import numpy.matlib
>>> a0 = np.array(1)
>>> np.matlib.repmat(a0, 2, 3)
array([[1, 1, 1],
       [1, 1, 1]])

>>> a1 = np.arange(4)
>>> np.matlib.repmat(a1, 2, 2)
array([[0, 1, 2, 3, 0, 1, 2, 3],
       [0, 1, 2, 3, 0, 1, 2, 3]])

>>> a2 = np.asmatrix(np.arange(6).reshape(2, 3))
>>> np.matlib.repmat(a2, 2, 3)
matrix([[0, 1, 2, 0, 1, 2, 0, 1, 2],
        [3, 4, 5, 3, 4, 5, 3, 4, 5],
        [0, 1, 2, 0, 1, 2, 0, 1, 2],
        [3, 4, 5, 3, 4, 5, 3, 4, 5]])
- `randn` (ID: 7c4feb27-5e33-41ec-bea1-8f38038e71d8): Return a random matrix with data from the "standard normal" distribution.

`randn` generates a matrix filled with random floats sampled from a
univariate "normal" (Gaussian) distribution of mean 0 and variance 1.

Parameters
----------
\*args : Arguments
    Shape of the output.
    If given as N integers, each integer specifies the size of one
    dimension. If given as a tuple, this tuple gives the complete shape.

Returns
-------
Z : matrix of floats
    A matrix of floating-point samples drawn from the standard normal
    distribution.

See Also
--------
rand, numpy.random.RandomState.randn

Notes
-----
For random samples from the normal distribution with mean ``mu`` and
standard deviation ``sigma``, use::

    sigma * np.matlib.randn(...) + mu

Examples
--------
>>> np.random.seed(123)
>>> import numpy.matlib
>>> np.matlib.randn(1)
matrix([[-1.0856306]])
>>> np.matlib.randn(1, 2, 3)
matrix([[ 0.99734545,  0.2829785 , -1.50629471],
        [-0.57860025,  1.65143654, -2.42667924]])

Two-by-four matrix of samples from the normal distribution with
mean 3 and standard deviation 2.5:

>>> 2.5 * np.matlib.randn((2, 4)) + 3
matrix([[1.92771843, 6.16484065, 0.83314899, 1.30278462],
        [2.76322758, 6.72847407, 1.40274501, 1.8900451 ]])
- `rand` (ID: 8de226dd-690d-4a7f-a842-7a5555122101): Return a matrix of random values with given shape.

Create a matrix of the given shape and propagate it with
random samples from a uniform distribution over ``[0, 1)``.

Parameters
----------
\*args : Arguments
    Shape of the output.
    If given as N integers, each integer specifies the size of one
    dimension.
    If given as a tuple, this tuple gives the complete shape.

Returns
-------
out : ndarray
    The matrix of random values with shape given by `\*args`.

See Also
--------
randn, numpy.random.RandomState.rand

Examples
--------
>>> np.random.seed(123)
>>> import numpy.matlib
>>> np.matlib.rand(2, 3)
matrix([[0.69646919, 0.28613933, 0.22685145],
        [0.55131477, 0.71946897, 0.42310646]])
>>> np.matlib.rand((2, 3))
matrix([[0.9807642 , 0.68482974, 0.4809319 ],
        [0.39211752, 0.34317802, 0.72904971]])

If the first argument is a tuple, other arguments are ignored:

>>> np.matlib.rand((2, 3), 4)
matrix([[0.43857224, 0.0596779 , 0.39804426],
        [0.73799541, 0.18249173, 0.17545176]])
- `ones` (ID: 154f64c6-2dd2-4891-b093-1d4420119237): Matrix of ones.

Return a matrix of given shape and type, filled with ones.

Parameters
----------
shape : {sequence of ints, int}
    Shape of the matrix
dtype : data-type, optional
    The desired data-type for the matrix, default is np.float64.
order : {'C', 'F'}, optional
    Whether to store matrix in C- or Fortran-contiguous order,
    default is 'C'.

Returns
-------
out : matrix
    Matrix of ones of given shape, dtype, and order.

See Also
--------
ones : Array of ones.
matlib.zeros : Zero matrix.

Notes
-----
If `shape` has length one i.e. ``(N,)``, or is a scalar ``N``,
`out` becomes a single row matrix of shape ``(1,N)``.

Examples
--------
>>> np.matlib.ones((2,3))
matrix([[1.,  1.,  1.],
        [1.,  1.,  1.]])

>>> np.matlib.ones(2)
matrix([[1.,  1.]])
- `identity` (ID: 469abd97-5b09-4c35-8225-0f14498634e7): Returns the square identity matrix of given size.

Parameters
----------
n : int
    Size of the returned identity matrix.
dtype : data-type, optional
    Data-type of the output. Defaults to ``float``.

Returns
-------
out : matrix
    `n` x `n` matrix with its main diagonal set to one,
    and all other elements zero.

See Also
--------
numpy.identity : Equivalent array function.
matlib.eye : More general matrix identity function.

Examples
--------
>>> import numpy.matlib
>>> np.matlib.identity(3, dtype=int)
matrix([[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
- `eye` (ID: 4b72159b-bd2e-4d1c-9efe-6380fc7dcb78): Return a matrix with ones on the diagonal and zeros elsewhere.

Parameters
----------
n : int
    Number of rows in the output.
M : int, optional
    Number of columns in the output, defaults to `n`.
k : int, optional
    Index of the diagonal: 0 refers to the main diagonal,
    a positive value refers to an upper diagonal,
    and a negative value to a lower diagonal.
dtype : dtype, optional
    Data-type of the returned matrix.
order : {'C', 'F'}, optional
    Whether the output should be stored in row-major (C-style) or
    column-major (Fortran-style) order in memory.

Returns
-------
I : matrix
    A `n` x `M` matrix where all elements are equal to zero,
    except for the `k`-th diagonal, whose values are equal to one.

See Also
--------
numpy.eye : Equivalent array function.
identity : Square identity matrix.

Examples
--------
>>> import numpy.matlib
>>> np.matlib.eye(3, k=1, dtype=float)
matrix([[0.,  1.,  0.],
        [0.,  0.,  1.],
        [0.,  0.,  0.]])
- `empty` (ID: 823d2dae-fe66-447f-bb03-a4669ac70e2a): Return a new matrix of given shape and type, without initializing entries.

Parameters
----------
shape : int or tuple of int
    Shape of the empty matrix.
dtype : data-type, optional
    Desired output data-type.
order : {'C', 'F'}, optional
    Whether to store multi-dimensional data in row-major
    (C-style) or column-major (Fortran-style) order in
    memory.

See Also
--------
numpy.empty : Equivalent array function.
matlib.zeros : Return a matrix of zeros.
matlib.ones : Return a matrix of ones.

Notes
-----
Unlike other matrix creation functions (e.g. `matlib.zeros`,
`matlib.ones`), `matlib.empty` does not initialize the values of the
matrix, and may therefore be marginally faster. However, the values
stored in the newly allocated matrix are arbitrary. For reproducible
behavior, be sure to set each element of the matrix before reading.

Examples
--------
>>> import numpy.matlib
>>> np.matlib.empty((2, 2))    # filled with random data
matrix([[  6.76425276e-320,   9.79033856e-307], # random
        [  7.39337286e-309,   3.22135945e-309]])
>>> np.matlib.empty((2, 2), dtype=int)
matrix([[ 6600475,        0], # random
        [ 6586976, 22740995]])
- `test_array_no_inheritance` (ID: 30b00a6f-d6dd-4a87-8549-ed7034093a4d): No description
- `assert_startswith` (ID: 2f8e894a-df7e-4e18-94b5-7494814481f5): No description
- `eqmask` (ID: 06392a23-c780-4a34-acda-fac200020901): No description
- `eq` (ID: f06f2c55-7f00-4a23-802e-9285eef538b2): No description
- `test_record_array_with_object_field` (ID: 96a54174-9ada-48b4-a8d8-782d431bf6c4): No description
- `test_uint_fill_value_and_filled` (ID: f11ff7aa-184d-4e5d-b8d5-27d9719c7959): No description
- `test_ufunc_with_output` (ID: 1df70937-d35f-4979-9c35-20c928bdead8): No description
- `test_ufunc_with_out_varied` (ID: 3590576c-fc8b-4bfd-b991-0e3c606ea344): Test that masked arrays are immune to gh-10459
- `test_masked_array_no_copy` (ID: d1d50a24-308e-4ba6-a2fc-a166c757b8c7): No description
- `test_masked_array` (ID: 884b5efd-0d16-4297-88cd-34d5f0a237b6): No description
- `test_mask_shape_assignment_does_not_break_masked` (ID: 9775d00c-e2d9-4f6d-a99c-b6ba37f78e74): No description
- `test_gh_22556` (ID: 8a4cd50b-730c-4e29-b443-d24b0ed94a69): No description
- `test_gh_21022` (ID: b57f2502-ef24-4176-98a4-cdfc9f8e4581): No description
- `test_fieldless_void` (ID: bbbe6570-c36b-4966-a7a6-2b5a56843d00): No description
- `test_doc_note` (ID: 8a00d449-a9b6-4760-8a74-1b9852286138): No description
- `test_default_fill_value_complex` (ID: 8c64f5b1-2aad-4866-8420-513947f7b06a): No description
- `test_deepcopy_2d_obj` (ID: b7d861cc-94f9-428c-b4ed-22a4be8bb77c): No description
- `test_deepcopy_0d_obj` (ID: 529cb3dd-9a1a-4385-9c40-de116f525be9): No description
- `test_astype_mask_ordering` (ID: 3b151e9c-6361-45c8-b42f-be08393263a3): No description
- `test_astype_basic` (ID: 372f887a-abce-497c-a2ea-a74419877f96): No description
- `test_append_masked_array_along_axis` (ID: 8514f327-55e7-4c24-a83e-a88fe7be8399): No description
- `test_append_masked_array` (ID: bf906e24-8fb8-4cc8-b283-82b99f75ed02): No description
- `test_matrix_transpose_raises_error_for_1d` (ID: 9649c06c-11cd-47b6-bee9-22ffe668e8ff): No description
- `test_matrix_transpose_equals_transpose_2d` (ID: 1c2a0028-c3a2-44f2-a6f2-ab17e9c1a177): No description
- `test_matrix_transpose_equals_swapaxes` (ID: e4e4ea3b-c732-44f4-9a85-d50b6078c0ed): No description
- `fromtextfile` (ID: 416b5fbd-580d-4b10-a007-db301a818258): Creates a mrecarray from data stored in the file `filename`.

Parameters
----------
fname : {file name/handle}
    Handle of an opened file.
delimiter : {None, string}, optional
    Alphanumeric character used to separate columns in the file.
    If None, any (group of) white spacestring(s) will be used.
commentchar : {'#', string}, optional
    Alphanumeric character used to mark the start of a comment.
missingchar : {'', string}, optional
    String indicating missing data, and used to create the masks.
varnames : {None, sequence}, optional
    Sequence of the variable names. If None, a list will be created from
    the first non empty line of the file.
vartypes : {None, sequence}, optional
    Sequence of the variables dtypes. If None, it will be estimated from
    the first non-commented line.


Ultra simple: the varnames are in the header, one line
- `fromrecords` (ID: 87fe6680-f23d-4344-ac57-0e4cd1fa07f3): Creates a MaskedRecords from a list of records.

Parameters
----------
reclist : sequence
    A list of records. Each element of the sequence is first converted
    to a masked array if needed. If a 2D array is passed as argument, it is
    processed line by line
dtype : {None, dtype}, optional
    Data type descriptor.
shape : {None,int}, optional
    Number of records. If None, ``shape`` is defined from the shape of the
    first array in the list.
formats : {None, sequence}, optional
    Sequence of formats for each individual field. If None, the formats will
    be autodetected by inspecting the fields and selecting the highest dtype
    possible.
names : {None, sequence}, optional
    Sequence of the names of each field.
fill_value : {None, sequence}, optional
    Sequence of data to be used as filling values.
mask : {nomask, sequence}, optional.
    External mask to apply on the data.

Notes
-----
Lists of tuples should be preferred over lists of lists for faster processing.
- `fromarrays` (ID: 588ae724-c738-4b39-9c2d-92d5bb43c5fb): Creates a mrecarray from a (flat) list of masked arrays.

Parameters
----------
arraylist : sequence
    A list of (masked) arrays. Each element of the sequence is first converted
    to a masked array if needed. If a 2D array is passed as argument, it is
    processed line by line
dtype : {None, dtype}, optional
    Data type descriptor.
shape : {None, integer}, optional
    Number of records. If None, shape is defined from the shape of the
    first array in the list.
formats : {None, sequence}, optional
    Sequence of formats for each individual field. If None, the formats will
    be autodetected by inspecting the fields and selecting the highest dtype
    possible.
names : {None, sequence}, optional
    Sequence of the names of each field.
fill_value : {None, sequence}, optional
    Sequence of data to be used as filling values.

Notes
-----
Lists of tuples should be preferred over lists of lists for faster processing.
- `addfield` (ID: 7e85b3a5-482a-4e5e-a307-2f1a0cd410f5): Adds a new field to the masked record array

Uses `newfield` as data and `newfieldname` as name. If `newfieldname`
is None, the new field name is set to 'fi', where `i` is the number of
existing fields.
- `vander` (ID: f8a27d57-303d-4c1a-8b57-47b6d62bb9f4): Masked values in the input array result in rows of zeros.
- `unique` (ID: e15e4203-af6c-4c96-afc9-0569f23ffddb): Finds the unique elements of an array.

Masked values are considered the same element (masked). The output array
is always a masked array. See `numpy.unique` for more details.

See Also
--------
numpy.unique : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> a = [1, 2, 1000, 2, 3]
>>> mask = [0, 0, 1, 0, 0]
>>> masked_a = np.ma.masked_array(a, mask)
>>> masked_a
masked_array(data=[1, 2, --, 2, 3],
            mask=[False, False,  True, False, False],
    fill_value=999999)
>>> np.ma.unique(masked_a)
masked_array(data=[1, 2, 3, --],
            mask=[False, False, False,  True],
    fill_value=999999)
>>> np.ma.unique(masked_a, return_index=True)
(masked_array(data=[1, 2, 3, --],
            mask=[False, False, False,  True],
    fill_value=999999), array([0, 1, 4, 2]))
>>> np.ma.unique(masked_a, return_inverse=True)
(masked_array(data=[1, 2, 3, --],
            mask=[False, False, False,  True],
    fill_value=999999), array([0, 1, 3, 1, 2]))
>>> np.ma.unique(masked_a, return_index=True, return_inverse=True)
(masked_array(data=[1, 2, 3, --],
            mask=[False, False, False,  True],
    fill_value=999999), array([0, 1, 4, 2]), array([0, 1, 3, 1, 2]))
- `union1d` (ID: cc21f910-cc39-42a6-a6be-fd045602f27d): Union of two arrays.

The output is always a masked array. See `numpy.union1d` for more details.

See Also
--------
numpy.union1d : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> ar1 = np.ma.array([1, 2, 3, 4])
>>> ar2 = np.ma.array([3, 4, 5, 6])
>>> np.ma.union1d(ar1, ar2)
masked_array(data=[1, 2, 3, 4, 5, 6],
         mask=False,
   fill_value=999999)
- `setxor1d` (ID: ba9d6a2e-c6ff-4efe-b4c1-b16d5d0d9c3a): Set exclusive-or of 1-D arrays with unique elements.

The output is always a masked array. See `numpy.setxor1d` for more details.

See Also
--------
numpy.setxor1d : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> ar1 = np.ma.array([1, 2, 3, 2, 4])
>>> ar2 = np.ma.array([2, 3, 5, 7, 5])
>>> np.ma.setxor1d(ar1, ar2)
masked_array(data=[1, 4, 5, 7],
             mask=False,
       fill_value=999999)
- `setdiff1d` (ID: e218070a-fc74-4d97-9041-4f596f887eea): Set difference of 1D arrays with unique elements.

The output is always a masked array. See `numpy.setdiff1d` for more
details.

See Also
--------
numpy.setdiff1d : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array([1, 2, 3, 4], mask=[0, 1, 0, 1])
>>> np.ma.setdiff1d(x, [1, 2])
masked_array(data=[3, --],
             mask=[False,  True],
       fill_value=999999)
- `polyfit` (ID: 191f7ef8-af03-4c5b-90dd-7eaba55a7ad6): Any masked values in x is propagated in y, and vice-versa.
- `notmasked_edges` (ID: c5ec51ae-047a-4e47-9cdb-f7ce95457a06): Find the indices of the first and last unmasked values along an axis.

If all values are masked, return None.  Otherwise, return a list
of two tuples, corresponding to the indices of the first and last
unmasked values respectively.

Parameters
----------
a : array_like
    The input array.
axis : int, optional
    Axis along which to perform the operation.
    If None (default), applies to a flattened version of the array.

Returns
-------
edges : ndarray or list
    An array of start and end indexes if there are any masked data in
    the array. If there are no masked data in the array, `edges` is a
    list of the first and last index.

See Also
--------
flatnotmasked_contiguous, flatnotmasked_edges, notmasked_contiguous
clump_masked, clump_unmasked

Examples
--------
>>> import numpy as np
>>> a = np.arange(9).reshape((3, 3))
>>> m = np.zeros_like(a)
>>> m[1:, 1:] = 1

>>> am = np.ma.array(a, mask=m)
>>> np.array(am[~am.mask])
array([0, 1, 2, 3, 6])

>>> np.ma.notmasked_edges(am)
array([0, 6])
- `notmasked_contiguous` (ID: feae942d-158d-4adc-9752-0a50d9fd784e): Find contiguous unmasked data in a masked array along the given axis.

Parameters
----------
a : array_like
    The input array.
axis : int, optional
    Axis along which to perform the operation.
    If None (default), applies to a flattened version of the array, and this
    is the same as `flatnotmasked_contiguous`.

Returns
-------
endpoints : list
    A list of slices (start and end indexes) of unmasked indexes
    in the array.

    If the input is 2d and axis is specified, the result is a list of lists.

See Also
--------
flatnotmasked_edges, flatnotmasked_contiguous, notmasked_edges
clump_masked, clump_unmasked

Notes
-----
Only accepts 2-D arrays at most.

Examples
--------
>>> import numpy as np
>>> a = np.arange(12).reshape((3, 4))
>>> mask = np.zeros_like(a)
>>> mask[1:, :-1] = 1; mask[0, 1] = 1; mask[-1, 0] = 0
>>> ma = np.ma.array(a, mask=mask)
>>> ma
masked_array(
  data=[[0, --, 2, 3],
        [--, --, --, 7],
        [8, --, --, 11]],
  mask=[[False,  True, False, False],
        [ True,  True,  True, False],
        [False,  True,  True, False]],
  fill_value=999999)
>>> np.array(ma[~ma.mask])
array([ 0,  2,  3,  7, 8, 11])

>>> np.ma.notmasked_contiguous(ma)
[slice(0, 1, None), slice(2, 4, None), slice(7, 9, None), slice(11, 12, None)]

>>> np.ma.notmasked_contiguous(ma, axis=0)
[[slice(0, 1, None), slice(2, 3, None)], [], [slice(0, 1, None)], [slice(0, 3, None)]]

>>> np.ma.notmasked_contiguous(ma, axis=1)
[[slice(0, 1, None), slice(2, 4, None)], [slice(3, 4, None)], [slice(0, 1, None), slice(3, 4, None)]]
- `ndenumerate` (ID: 87fc1d89-6edd-49d7-9e74-02e05819ad32): Multidimensional index iterator.

Return an iterator yielding pairs of array coordinates and values,
skipping elements that are masked. With `compressed=False`,
`ma.masked` is yielded as the value of masked elements. This
behavior differs from that of `numpy.ndenumerate`, which yields the
value of the underlying data array.

Notes
-----
.. versionadded:: 1.23.0

Parameters
----------
a : array_like
    An array with (possibly) masked elements.
compressed : bool, optional
    If True (default), masked elements are skipped.

See Also
--------
numpy.ndenumerate : Equivalent function ignoring any mask.

Examples
--------
>>> import numpy as np
>>> a = np.ma.arange(9).reshape((3, 3))
>>> a[1, 0] = np.ma.masked
>>> a[1, 2] = np.ma.masked
>>> a[2, 1] = np.ma.masked
>>> a
masked_array(
  data=[[0, 1, 2],
        [--, 4, --],
        [6, --, 8]],
  mask=[[False, False, False],
        [ True, False,  True],
        [False,  True, False]],
  fill_value=999999)
>>> for index, x in np.ma.ndenumerate(a):
...     print(index, x)
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 1) 4
(2, 0) 6
(2, 2) 8

>>> for index, x in np.ma.ndenumerate(a, compressed=False):
...     print(index, x)
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 0) --
(1, 1) 4
(1, 2) --
(2, 0) 6
(2, 1) --
(2, 2) 8
- `median` (ID: 1528310e-e6e5-43cc-8c75-6a26e80b1be3): Compute the median along the specified axis.

Returns the median of the array elements.

Parameters
----------
a : array_like
    Input array or object that can be converted to an array.
axis : int, optional
    Axis along which the medians are computed. The default (None) is
    to compute the median along a flattened version of the array.
out : ndarray, optional
    Alternative output array in which to place the result. It must
    have the same shape and buffer length as the expected output
    but the type will be cast if necessary.
overwrite_input : bool, optional
    If True, then allow use of memory of input array (a) for
    calculations. The input array will be modified by the call to
    median. This will save memory when you do not need to preserve
    the contents of the input array. Treat the input as undefined,
    but it will probably be fully or partially sorted. Default is
    False. Note that, if `overwrite_input` is True, and the input
    is not already an `ndarray`, an error will be raised.
keepdims : bool, optional
    If this is set to True, the axes which are reduced are left
    in the result as dimensions with size one. With this option,
    the result will broadcast correctly against the input array.

Returns
-------
median : ndarray
    A new array holding the result is returned unless out is
    specified, in which case a reference to out is returned.
    Return data-type is `float64` for integers and floats smaller than
    `float64`, or the input data-type, otherwise.

See Also
--------
mean

Notes
-----
Given a vector ``V`` with ``N`` non masked values, the median of ``V``
is the middle value of a sorted copy of ``V`` (``Vs``) - i.e.
``Vs[(N-1)/2]``, when ``N`` is odd, or ``{Vs[N/2 - 1] + Vs[N/2]}/2``
when ``N`` is even.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array(np.arange(8), mask=[0]*4 + [1]*4)
>>> np.ma.median(x)
1.5

>>> x = np.ma.array(np.arange(10).reshape(2, 5), mask=[0]*6 + [1]*4)
>>> np.ma.median(x)
2.5
>>> np.ma.median(x, axis=-1, overwrite_input=True)
masked_array(data=[2.0, 5.0],
             mask=[False, False],
       fill_value=1e+20)
- `masked_all_like` (ID: 025f66f3-aa42-4699-9d1a-4e4cecf00d7f): Empty masked array with the properties of an existing array.

Return an empty masked array of the same shape and dtype as
the array `arr`, where all the data are masked.

Parameters
----------
arr : ndarray
    An array describing the shape and dtype of the required MaskedArray.

Returns
-------
a : MaskedArray
    A masked array with all data masked.

Raises
------
AttributeError
    If `arr` doesn't have a shape attribute (i.e. not an ndarray)

See Also
--------
masked_all : Empty masked array with all elements masked.

Notes
-----
Unlike other masked array creation functions (e.g. `numpy.ma.zeros_like`,
`numpy.ma.ones_like`, `numpy.ma.full_like`), `masked_all_like` does not
initialize the values of the array, and may therefore be marginally
faster. However, the values stored in the newly allocated array are
arbitrary. For reproducible behavior, be sure to set each element of the
array before reading.

Examples
--------
>>> import numpy as np
>>> arr = np.zeros((2, 3), dtype=np.float32)
>>> arr
array([[0., 0., 0.],
       [0., 0., 0.]], dtype=float32)
>>> np.ma.masked_all_like(arr)
masked_array(
  data=[[--, --, --],
        [--, --, --]],
  mask=[[ True,  True,  True],
        [ True,  True,  True]],
  fill_value=np.float64(1e+20),
  dtype=float32)

The dtype of the masked array matches the dtype of `arr`.

>>> arr.dtype
dtype('float32')
>>> np.ma.masked_all_like(arr).dtype
dtype('float32')
- `masked_all` (ID: c85392ae-698c-4ca7-9076-3a98f7ceba9b): Empty masked array with all elements masked.

Return an empty masked array of the given shape and dtype, where all the
data are masked.

Parameters
----------
shape : int or tuple of ints
    Shape of the required MaskedArray, e.g., ``(2, 3)`` or ``2``.
dtype : dtype, optional
    Data type of the output.

Returns
-------
a : MaskedArray
    A masked array with all data masked.

See Also
--------
masked_all_like : Empty masked array modelled on an existing array.

Notes
-----
Unlike other masked array creation functions (e.g. `numpy.ma.zeros`,
`numpy.ma.ones`, `numpy.ma.full`), `masked_all` does not initialize the
values of the array, and may therefore be marginally faster. However,
the values stored in the newly allocated array are arbitrary. For
reproducible behavior, be sure to set each element of the array before
reading.

Examples
--------
>>> import numpy as np
>>> np.ma.masked_all((3, 3))
masked_array(
  data=[[--, --, --],
        [--, --, --],
        [--, --, --]],
  mask=[[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]],
  fill_value=1e+20,
  dtype=float64)

The `dtype` parameter defines the underlying data type.

>>> a = np.ma.masked_all((3, 3))
>>> a.dtype
dtype('float64')
>>> a = np.ma.masked_all((3, 3), dtype=np.int32)
>>> a.dtype
dtype('int32')
- `mask_rows` (ID: 08e8e1b0-3f48-4594-9d50-ff291006638f): Mask rows of a 2D array that contain masked values.

This function is a shortcut to ``mask_rowcols`` with `axis` equal to 0.

See Also
--------
mask_rowcols : Mask rows and/or columns of a 2D array.
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> a = np.zeros((3, 3), dtype=int)
>>> a[1, 1] = 1
>>> a
array([[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]])
>>> a = np.ma.masked_equal(a, 1)
>>> a
masked_array(
  data=[[0, 0, 0],
        [0, --, 0],
        [0, 0, 0]],
  mask=[[False, False, False],
        [False,  True, False],
        [False, False, False]],
  fill_value=1)

>>> np.ma.mask_rows(a)
masked_array(
  data=[[0, 0, 0],
        [--, --, --],
        [0, 0, 0]],
  mask=[[False, False, False],
        [ True,  True,  True],
        [False, False, False]],
  fill_value=1)
- `mask_rowcols` (ID: c3850a49-78b7-409f-8e29-ca75d52ef657): Mask rows and/or columns of a 2D array that contain masked values.

Mask whole rows and/or columns of a 2D array that contain
masked values.  The masking behavior is selected using the
`axis` parameter.

  - If `axis` is None, rows *and* columns are masked.
  - If `axis` is 0, only rows are masked.
  - If `axis` is 1 or -1, only columns are masked.

Parameters
----------
a : array_like, MaskedArray
    The array to mask.  If not a MaskedArray instance (or if no array
    elements are masked), the result is a MaskedArray with `mask` set
    to `nomask` (False). Must be a 2D array.
axis : int, optional
    Axis along which to perform the operation. If None, applies to a
    flattened version of the array.

Returns
-------
a : MaskedArray
    A modified version of the input array, masked depending on the value
    of the `axis` parameter.

Raises
------
NotImplementedError
    If input array `a` is not 2D.

See Also
--------
mask_rows : Mask rows of a 2D array that contain masked values.
mask_cols : Mask cols of a 2D array that contain masked values.
masked_where : Mask where a condition is met.

Notes
-----
The input array's mask is modified by this function.

Examples
--------
>>> import numpy as np
>>> a = np.zeros((3, 3), dtype=int)
>>> a[1, 1] = 1
>>> a
array([[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]])
>>> a = np.ma.masked_equal(a, 1)
>>> a
masked_array(
  data=[[0, 0, 0],
        [0, --, 0],
        [0, 0, 0]],
  mask=[[False, False, False],
        [False,  True, False],
        [False, False, False]],
  fill_value=1)
>>> np.ma.mask_rowcols(a)
masked_array(
  data=[[0, --, 0],
        [--, --, --],
        [0, --, 0]],
  mask=[[False,  True, False],
        [ True,  True,  True],
        [False,  True, False]],
  fill_value=1)
- `mask_cols` (ID: 077d2662-15f5-4daa-9517-6492ef36eaa2): Mask columns of a 2D array that contain masked values.

This function is a shortcut to ``mask_rowcols`` with `axis` equal to 1.

See Also
--------
mask_rowcols : Mask rows and/or columns of a 2D array.
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> a = np.zeros((3, 3), dtype=int)
>>> a[1, 1] = 1
>>> a
array([[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]])
>>> a = np.ma.masked_equal(a, 1)
>>> a
masked_array(
  data=[[0, 0, 0],
        [0, --, 0],
        [0, 0, 0]],
  mask=[[False, False, False],
        [False,  True, False],
        [False, False, False]],
  fill_value=1)
>>> np.ma.mask_cols(a)
masked_array(
  data=[[0, --, 0],
        [0, --, 0],
        [0, --, 0]],
  mask=[[False,  True, False],
        [False,  True, False],
        [False,  True, False]],
  fill_value=1)
- `isin` (ID: e32f3b6b-e1a4-4a17-869d-7d0e6ea26389): Calculates `element in test_elements`, broadcasting over
`element` only.

The output is always a masked array of the same shape as `element`.
See `numpy.isin` for more details.

See Also
--------
in1d       : Flattened version of this function.
numpy.isin : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> element = np.ma.array([1, 2, 3, 4, 5, 6])
>>> test_elements = [0, 2]
>>> np.ma.isin(element, test_elements)
masked_array(data=[False,  True, False, False, False, False],
             mask=False,
       fill_value=True)
- `intersect1d` (ID: f61dbfa2-94a7-41c2-b15c-4b8972948f4d): Returns the unique elements common to both arrays.

Masked values are considered equal one to the other.
The output is always a masked array.

See `numpy.intersect1d` for more details.

See Also
--------
numpy.intersect1d : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array([1, 3, 3, 3], mask=[0, 0, 0, 1])
>>> y = np.ma.array([3, 1, 1, 1], mask=[0, 0, 0, 1])
>>> np.ma.intersect1d(x, y)
masked_array(data=[1, 3, --],
             mask=[False, False,  True],
       fill_value=999999)
- `in1d` (ID: 05a40fe0-0f95-414b-b240-2687734f9683): Test whether each element of an array is also present in a second
array.

The output is always a masked array. See `numpy.in1d` for more details.

We recommend using :func:`isin` instead of `in1d` for new code.

See Also
--------
isin       : Version of this function that preserves the shape of ar1.
numpy.in1d : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> ar1 = np.ma.array([0, 1, 2, 5, 0])
>>> ar2 = [0, 2]
>>> np.ma.in1d(ar1, ar2)
masked_array(data=[ True, False,  True, False,  True],
             mask=False,
       fill_value=True)
- `flatnotmasked_edges` (ID: ea5b1a1d-0351-4c09-bf19-e8f4eec3c202): Find the indices of the first and last unmasked values.

Expects a 1-D `MaskedArray`, returns None if all values are masked.

Parameters
----------
a : array_like
    Input 1-D `MaskedArray`

Returns
-------
edges : ndarray or None
    The indices of first and last non-masked value in the array.
    Returns None if all values are masked.

See Also
--------
flatnotmasked_contiguous, notmasked_contiguous, notmasked_edges
clump_masked, clump_unmasked

Notes
-----
Only accepts 1-D arrays.

Examples
--------
>>> import numpy as np
>>> a = np.ma.arange(10)
>>> np.ma.flatnotmasked_edges(a)
array([0, 9])

>>> mask = (a < 3) | (a > 8) | (a == 5)
>>> a[mask] = np.ma.masked
>>> np.array(a[~a.mask])
array([3, 4, 6, 7, 8])

>>> np.ma.flatnotmasked_edges(a)
array([3, 8])

>>> a[:] = np.ma.masked
>>> print(np.ma.flatnotmasked_edges(a))
None
- `flatnotmasked_contiguous` (ID: 2b41678c-9a74-45b0-970a-bb31c125cd66): Find contiguous unmasked data in a masked array.

Parameters
----------
a : array_like
    The input array.

Returns
-------
slice_list : list
    A sorted sequence of `slice` objects (start index, end index).

See Also
--------
flatnotmasked_edges, notmasked_contiguous, notmasked_edges
clump_masked, clump_unmasked

Notes
-----
Only accepts 2-D arrays at most.

Examples
--------
>>> import numpy as np
>>> a = np.ma.arange(10)
>>> np.ma.flatnotmasked_contiguous(a)
[slice(0, 10, None)]

>>> mask = (a < 3) | (a > 8) | (a == 5)
>>> a[mask] = np.ma.masked
>>> np.array(a[~a.mask])
array([3, 4, 6, 7, 8])

>>> np.ma.flatnotmasked_contiguous(a)
[slice(3, 5, None), slice(6, 9, None)]
>>> a[:] = np.ma.masked
>>> np.ma.flatnotmasked_contiguous(a)
[]
- `ediff1d` (ID: 002da909-e1f1-413b-abb6-1b9acfe62f9e): Compute the differences between consecutive elements of an array.

This function is the equivalent of `numpy.ediff1d` that takes masked
values into account, see `numpy.ediff1d` for details.

See Also
--------
numpy.ediff1d : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np
>>> arr = np.ma.array([1, 2, 4, 7, 0])
>>> np.ma.ediff1d(arr)
masked_array(data=[ 1,  2,  3, -7],
             mask=False,
       fill_value=999999)
- `cov` (ID: f0c3c9a2-1a87-48cf-8a42-f7a2eb2b31f3): Estimate the covariance matrix.

Except for the handling of missing data this function does the same as
`numpy.cov`. For more details and examples, see `numpy.cov`.

By default, masked values are recognized as such. If `x` and `y` have the
same shape, a common mask is allocated: if ``x[i,j]`` is masked, then
``y[i,j]`` will also be masked.
Setting `allow_masked` to False will raise an exception if values are
missing in either of the input arrays.

Parameters
----------
x : array_like
    A 1-D or 2-D array containing multiple variables and observations.
    Each row of `x` represents a variable, and each column a single
    observation of all those variables. Also see `rowvar` below.
y : array_like, optional
    An additional set of variables and observations. `y` has the same
    shape as `x`.
rowvar : bool, optional
    If `rowvar` is True (default), then each row represents a
    variable, with observations in the columns. Otherwise, the relationship
    is transposed: each column represents a variable, while the rows
    contain observations.
bias : bool, optional
    Default normalization (False) is by ``(N-1)``, where ``N`` is the
    number of observations given (unbiased estimate). If `bias` is True,
    then normalization is by ``N``. This keyword can be overridden by
    the keyword ``ddof`` in numpy versions >= 1.5.
allow_masked : bool, optional
    If True, masked values are propagated pair-wise: if a value is masked
    in `x`, the corresponding value is masked in `y`.
    If False, raises a `ValueError` exception when some values are missing.
ddof : {None, int}, optional
    If not ``None`` normalization is by ``(N - ddof)``, where ``N`` is
    the number of observations; this overrides the value implied by
    ``bias``. The default value is ``None``.

Raises
------
ValueError
    Raised if some values are missing and `allow_masked` is False.

See Also
--------
numpy.cov

Examples
--------
>>> import numpy as np
>>> x = np.ma.array([[0, 1], [1, 1]], mask=[0, 1, 0, 1])
>>> y = np.ma.array([[1, 0], [0, 1]], mask=[0, 0, 1, 1])
>>> np.ma.cov(x, y)
masked_array(
data=[[--, --, --, --],
      [--, --, --, --],
      [--, --, --, --],
      [--, --, --, --]],
mask=[[ True,  True,  True,  True],
      [ True,  True,  True,  True],
      [ True,  True,  True,  True],
      [ True,  True,  True,  True]],
fill_value=1e+20,
dtype=float64)
- `count_masked` (ID: 6183b2de-698e-4034-9593-957e673844f8): Count the number of masked elements along the given axis.

Parameters
----------
arr : array_like
    An array with (possibly) masked elements.
axis : int, optional
    Axis along which to count. If None (default), a flattened
    version of the array is used.

Returns
-------
count : int, ndarray
    The total number of masked elements (axis=None) or the number
    of masked elements along each slice of the given axis.

See Also
--------
MaskedArray.count : Count non-masked elements.

Examples
--------
>>> import numpy as np
>>> a = np.arange(9).reshape((3,3))
>>> a = np.ma.array(a)
>>> a[1, 0] = np.ma.masked
>>> a[1, 2] = np.ma.masked
>>> a[2, 1] = np.ma.masked
>>> a
masked_array(
  data=[[0, 1, 2],
        [--, 4, --],
        [6, --, 8]],
  mask=[[False, False, False],
        [ True, False,  True],
        [False,  True, False]],
  fill_value=999999)
>>> np.ma.count_masked(a)
3

When the `axis` keyword is used an array is returned.

>>> np.ma.count_masked(a, axis=0)
array([1, 1, 1])
>>> np.ma.count_masked(a, axis=1)
array([0, 2, 1])
- `corrcoef` (ID: f84e8720-bcf3-489b-9b2a-f67035e874c3): Return Pearson product-moment correlation coefficients.

Except for the handling of missing data this function does the same as
`numpy.corrcoef`. For more details and examples, see `numpy.corrcoef`.

Parameters
----------
x : array_like
    A 1-D or 2-D array containing multiple variables and observations.
    Each row of `x` represents a variable, and each column a single
    observation of all those variables. Also see `rowvar` below.
y : array_like, optional
    An additional set of variables and observations. `y` has the same
    shape as `x`.
rowvar : bool, optional
    If `rowvar` is True (default), then each row represents a
    variable, with observations in the columns. Otherwise, the relationship
    is transposed: each column represents a variable, while the rows
    contain observations.
bias : _NoValue, optional
    Has no effect, do not use.

    .. deprecated:: 1.10.0
allow_masked : bool, optional
    If True, masked values are propagated pair-wise: if a value is masked
    in `x`, the corresponding value is masked in `y`.
    If False, raises an exception.  Because `bias` is deprecated, this
    argument needs to be treated as keyword only to avoid a warning.
ddof : _NoValue, optional
    Has no effect, do not use.

    .. deprecated:: 1.10.0

See Also
--------
numpy.corrcoef : Equivalent function in top-level NumPy module.
cov : Estimate the covariance matrix.

Notes
-----
This function accepts but discards arguments `bias` and `ddof`.  This is
for backwards compatibility with previous versions of this function.  These
arguments had no effect on the return values of the function and can be
safely ignored in this and previous versions of numpy.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array([[0, 1], [1, 1]], mask=[0, 1, 0, 1])
>>> np.ma.corrcoef(x)
masked_array(
  data=[[--, --],
        [--, --]],
  mask=[[ True,  True],
        [ True,  True]],
  fill_value=1e+20,
  dtype=float64)
- `compress_rows` (ID: 00eb96f3-b66e-4597-bce5-70b66e040c26): Suppress whole rows of a 2-D array that contain masked values.

This is equivalent to ``np.ma.compress_rowcols(a, 0)``, see
`compress_rowcols` for details.

Parameters
----------
x : array_like, MaskedArray
    The array to operate on. If not a MaskedArray instance (or if no array
    elements are masked), `x` is interpreted as a MaskedArray with
    `mask` set to `nomask`. Must be a 2D array.

Returns
-------
compressed_array : ndarray
    The compressed array.

See Also
--------
compress_rowcols

Examples
--------
>>> import numpy as np
>>> a = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
...                                                   [1, 0, 0],
...                                                   [0, 0, 0]])
>>> np.ma.compress_rows(a)
array([[6, 7, 8]])
- `compress_rowcols` (ID: 1dbdd9cc-1ef7-41f8-b89f-0ed05b8915bf): Suppress the rows and/or columns of a 2-D array that contain
masked values.

The suppression behavior is selected with the `axis` parameter.

- If axis is None, both rows and columns are suppressed.
- If axis is 0, only rows are suppressed.
- If axis is 1 or -1, only columns are suppressed.

Parameters
----------
x : array_like, MaskedArray
    The array to operate on.  If not a MaskedArray instance (or if no array
    elements are masked), `x` is interpreted as a MaskedArray with
    `mask` set to `nomask`. Must be a 2D array.
axis : int, optional
    Axis along which to perform the operation. Default is None.

Returns
-------
compressed_array : ndarray
    The compressed array.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
...                                                   [1, 0, 0],
...                                                   [0, 0, 0]])
>>> x
masked_array(
  data=[[--, 1, 2],
        [--, 4, 5],
        [6, 7, 8]],
  mask=[[ True, False, False],
        [ True, False, False],
        [False, False, False]],
  fill_value=999999)

>>> np.ma.compress_rowcols(x)
array([[7, 8]])
>>> np.ma.compress_rowcols(x, 0)
array([[6, 7, 8]])
>>> np.ma.compress_rowcols(x, 1)
array([[1, 2],
       [4, 5],
       [7, 8]])
- `compress_nd` (ID: 6a35ad7b-edc9-4e99-8c3f-e2982e591df2): Suppress slices from multiple dimensions which contain masked values.

Parameters
----------
x : array_like, MaskedArray
    The array to operate on. If not a MaskedArray instance (or if no array
    elements are masked), `x` is interpreted as a MaskedArray with `mask`
    set to `nomask`.
axis : tuple of ints or int, optional
    Which dimensions to suppress slices from can be configured with this
    parameter.
    - If axis is a tuple of ints, those are the axes to suppress slices from.
    - If axis is an int, then that is the only axis to suppress slices from.
    - If axis is None, all axis are selected.

Returns
-------
compress_array : ndarray
    The compressed array.

Examples
--------
>>> import numpy as np
>>> arr = [[1, 2], [3, 4]]
>>> mask = [[0, 1], [0, 0]]
>>> x = np.ma.array(arr, mask=mask)
>>> np.ma.compress_nd(x, axis=0)
array([[3, 4]])
>>> np.ma.compress_nd(x, axis=1)
array([[1],
       [3]])
>>> np.ma.compress_nd(x)
array([[3]])
- `compress_cols` (ID: 65ae9b87-8080-4ba5-b9cc-b852ca1264a2): Suppress whole columns of a 2-D array that contain masked values.

This is equivalent to ``np.ma.compress_rowcols(a, 1)``, see
`compress_rowcols` for details.

Parameters
----------
x : array_like, MaskedArray
    The array to operate on.  If not a MaskedArray instance (or if no array
    elements are masked), `x` is interpreted as a MaskedArray with
    `mask` set to `nomask`. Must be a 2D array.

Returns
-------
compressed_array : ndarray
    The compressed array.

See Also
--------
compress_rowcols

Examples
--------
>>> import numpy as np
>>> a = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
...                                                   [1, 0, 0],
...                                                   [0, 0, 0]])
>>> np.ma.compress_cols(a)
array([[1, 2],
       [4, 5],
       [7, 8]])
- `clump_unmasked` (ID: 8d7085dc-a9eb-435b-8817-abb6bfd827e3): Return list of slices corresponding to the unmasked clumps of a 1-D array.
(A "clump" is defined as a contiguous region of the array).

Parameters
----------
a : ndarray
    A one-dimensional masked array.

Returns
-------
slices : list of slice
    The list of slices, one for each continuous region of unmasked
    elements in `a`.

See Also
--------
flatnotmasked_edges, flatnotmasked_contiguous, notmasked_edges
notmasked_contiguous, clump_masked

Examples
--------
>>> import numpy as np
>>> a = np.ma.masked_array(np.arange(10))
>>> a[[0, 1, 2, 6, 8, 9]] = np.ma.masked
>>> np.ma.clump_unmasked(a)
[slice(3, 6, None), slice(7, 8, None)]
- `clump_masked` (ID: dbc937e6-21e6-4412-8695-df9abc967c4a): Returns a list of slices corresponding to the masked clumps of a 1-D array.
(A "clump" is defined as a contiguous region of the array).

Parameters
----------
a : ndarray
    A one-dimensional masked array.

Returns
-------
slices : list of slice
    The list of slices, one for each continuous region of masked elements
    in `a`.

See Also
--------
flatnotmasked_edges, flatnotmasked_contiguous, notmasked_edges
notmasked_contiguous, clump_unmasked

Examples
--------
>>> import numpy as np
>>> a = np.ma.masked_array(np.arange(10))
>>> a[[0, 1, 2, 6, 8, 9]] = np.ma.masked
>>> np.ma.clump_masked(a)
[slice(0, 3, None), slice(6, 7, None), slice(8, 10, None)]
- `average` (ID: 4c481fbf-5e6f-41ae-9d6b-766cbf71d00b): Return the weighted average of array over the given axis.

Parameters
----------
a : array_like
    Data to be averaged.
    Masked entries are not taken into account in the computation.
axis : None or int or tuple of ints, optional
    Axis or axes along which to average `a`.  The default,
    `axis=None`, will average over all of the elements of the input array.
    If axis is a tuple of ints, averaging is performed on all of the axes
    specified in the tuple instead of a single axis or all the axes as
    before.
weights : array_like, optional
    An array of weights associated with the values in `a`. Each value in
    `a` contributes to the average according to its associated weight.
    The array of weights must be the same shape as `a` if no axis is
    specified, otherwise the weights must have dimensions and shape
    consistent with `a` along the specified axis.
    If `weights=None`, then all data in `a` are assumed to have a
    weight equal to one.
    The calculation is::

        avg = sum(a * weights) / sum(weights)

    where the sum is over all included elements.
    The only constraint on the values of `weights` is that `sum(weights)`
    must not be 0.
returned : bool, optional
    Flag indicating whether a tuple ``(result, sum of weights)``
    should be returned as output (True), or just the result (False).
    Default is False.
keepdims : bool, optional
    If this is set to True, the axes which are reduced are left
    in the result as dimensions with size one. With this option,
    the result will broadcast correctly against the original `a`.
    *Note:* `keepdims` will not work with instances of `numpy.matrix`
    or other classes whose methods do not support `keepdims`.

    .. versionadded:: 1.23.0

Returns
-------
average, [sum_of_weights] : (tuple of) scalar or MaskedArray
    The average along the specified axis. When returned is `True`,
    return a tuple with the average as the first element and the sum
    of the weights as the second element. The return type is `np.float64`
    if `a` is of integer type and floats smaller than `float64`, or the
    input data-type, otherwise. If returned, `sum_of_weights` is always
    `float64`.

Raises
------
ZeroDivisionError
    When all weights along axis are zero. See `numpy.ma.average` for a
    version robust to this type of error.
TypeError
    When `weights` does not have the same shape as `a`, and `axis=None`.
ValueError
    When `weights` does not have dimensions and shape consistent with `a`
    along specified `axis`.

Examples
--------
>>> import numpy as np
>>> a = np.ma.array([1., 2., 3., 4.], mask=[False, False, True, True])
>>> np.ma.average(a, weights=[3, 1, 0, 0])
1.25

>>> x = np.ma.arange(6.).reshape(3, 2)
>>> x
masked_array(
  data=[[0., 1.],
        [2., 3.],
        [4., 5.]],
  mask=False,
  fill_value=1e+20)
>>> data = np.arange(8).reshape((2, 2, 2))
>>> data
array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])
>>> np.ma.average(data, axis=(0, 1), weights=[[1./4, 3./4], [1., 1./2]])
masked_array(data=[3.4, 4.4],
         mask=[False, False],
   fill_value=1e+20)
>>> np.ma.average(data, axis=0, weights=[[1./4, 3./4], [1., 1./2]])
Traceback (most recent call last):
    ...
ValueError: Shape of weights must be consistent
with shape of a along specified axis.

>>> avg, sumweights = np.ma.average(x, axis=0, weights=[1, 2, 3],
...                                 returned=True)
>>> avg
masked_array(data=[2.6666666666666665, 3.6666666666666665],
             mask=[False, False],
       fill_value=1e+20)

With ``keepdims=True``, the following result has shape (3, 1).

>>> np.ma.average(x, axis=1, keepdims=True)
masked_array(
  data=[[0.5],
        [2.5],
        [4.5]],
  mask=False,
  fill_value=1e+20)
- `apply_over_axes` (ID: d503bf9d-e693-4127-a3b3-351318008cd8): (This docstring will be overwritten)
- `apply_along_axis` (ID: 1dac541f-ee85-4032-9a1d-29d227eeb3c7): (This docstring should be overwritten)
- `where` (ID: bad3f842-76c4-4412-88be-fbbcbb9daa07): Return a masked array with elements from `x` or `y`, depending on condition.

.. note::
    When only `condition` is provided, this function is identical to
    `nonzero`. The rest of this documentation covers only the case where
    all three arguments are provided.

Parameters
----------
condition : array_like, bool
    Where True, yield `x`, otherwise yield `y`.
x, y : array_like, optional
    Values from which to choose. `x`, `y` and `condition` need to be
    broadcastable to some shape.

Returns
-------
out : MaskedArray
    An masked array with `masked` elements where the condition is masked,
    elements from `x` where `condition` is True, and elements from `y`
    elsewhere.

See Also
--------
numpy.where : Equivalent function in the top-level NumPy module.
nonzero : The function that is called when x and y are omitted

Examples
--------
>>> import numpy as np
>>> x = np.ma.array(np.arange(9.).reshape(3, 3), mask=[[0, 1, 0],
...                                                    [1, 0, 1],
...                                                    [0, 1, 0]])
>>> x
masked_array(
  data=[[0.0, --, 2.0],
        [--, 4.0, --],
        [6.0, --, 8.0]],
  mask=[[False,  True, False],
        [ True, False,  True],
        [False,  True, False]],
  fill_value=1e+20)
>>> np.ma.where(x > 5, x, -3.1416)
masked_array(
  data=[[-3.1416, --, -3.1416],
        [--, -3.1416, --],
        [6.0, --, 8.0]],
  mask=[[False,  True, False],
        [ True, False,  True],
        [False,  True, False]],
  fill_value=1e+20)
- `transpose` (ID: 19e2a956-c158-403d-8feb-823ca7f151ab): Permute the dimensions of an array.

This function is exactly equivalent to `numpy.transpose`.

See Also
--------
numpy.transpose : Equivalent function in top-level NumPy module.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = ma.arange(4).reshape((2,2))
>>> x[1, 1] = ma.masked
>>> x
masked_array(
  data=[[0, 1],
        [2, --]],
  mask=[[False, False],
        [False,  True]],
  fill_value=999999)

>>> ma.transpose(x)
masked_array(
  data=[[0, 2],
        [1, --]],
  mask=[[False, False],
        [False,  True]],
  fill_value=999999)
- `take` (ID: 4f457487-5f00-4462-ae15-fb0aec750e9c): 
- `sort` (ID: 196c260a-e890-401e-a8c1-1dab7c0c2167): Return a sorted copy of the masked array.

Equivalent to creating a copy of the array
and applying the  MaskedArray ``sort()`` method.

Refer to ``MaskedArray.sort`` for the full documentation

See Also
--------
MaskedArray.sort : equivalent method

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = [11.2, -3.973, 0.801, -1.41]
>>> mask = [0, 0, 0, 1]
>>> masked_x = ma.masked_array(x, mask)
>>> masked_x
masked_array(data=[11.2, -3.973, 0.801, --],
             mask=[False, False, False,  True],
       fill_value=1e+20)
>>> ma.sort(masked_x)
masked_array(data=[-3.973, 0.801, 11.2, --],
             mask=[False, False, False,  True],
       fill_value=1e+20)
- `size` (ID: 6abb32fb-a7dc-4d5d-bcd7-ab288e827aef): maskedarray version of the numpy function.
- `shape` (ID: bf4ceeaa-a2f8-44c6-9190-6c5098405142): maskedarray version of the numpy function.
- `set_fill_value` (ID: 922637d2-a9fc-4886-bdf0-21af0f5f3210): Set the filling value of a, if a is a masked array.

This function changes the fill value of the masked array `a` in place.
If `a` is not a masked array, the function returns silently, without
doing anything.

Parameters
----------
a : array_like
    Input array.
fill_value : dtype
    Filling value. A consistency test is performed to make sure
    the value is compatible with the dtype of `a`.

Returns
-------
None
    Nothing returned by this function.

See Also
--------
maximum_fill_value : Return the default fill value for a dtype.
MaskedArray.fill_value : Return current fill value.
MaskedArray.set_fill_value : Equivalent method.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> a = ma.masked_where(a < 3, a)
>>> a
masked_array(data=[--, --, --, 3, 4],
             mask=[ True,  True,  True, False, False],
       fill_value=999999)
>>> ma.set_fill_value(a, -999)
>>> a
masked_array(data=[--, --, --, 3, 4],
             mask=[ True,  True,  True, False, False],
       fill_value=-999)

Nothing happens if `a` is not a masked array.

>>> a = list(range(5))
>>> a
[0, 1, 2, 3, 4]
>>> ma.set_fill_value(a, 100)
>>> a
[0, 1, 2, 3, 4]
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> ma.set_fill_value(a, 100)
>>> a
array([0, 1, 2, 3, 4])
- `round_` (ID: 5d1d905e-0fca-4aee-8c10-b599255eef9e): Return a copy of a, rounded to 'decimals' places.

When 'decimals' is negative, it specifies the number of positions
to the left of the decimal point.  The real and imaginary parts of
complex numbers are rounded separately. Nothing is done if the
array is not of float type and 'decimals' is greater than or equal
to 0.

Parameters
----------
decimals : int
    Number of decimals to round to. May be negative.
out : array_like
    Existing array to use for output.
    If not given, returns a default copy of a.

Notes
-----
If out is given and does not have a mask attribute, the mask of a
is lost!

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = [11.2, -3.973, 0.801, -1.41]
>>> mask = [0, 0, 0, 1]
>>> masked_x = ma.masked_array(x, mask)
>>> masked_x
masked_array(data=[11.2, -3.973, 0.801, --],
             mask=[False, False, False, True],
    fill_value=1e+20)
>>> ma.round_(masked_x)
masked_array(data=[11.0, -4.0, 1.0, --],
             mask=[False, False, False, True],
    fill_value=1e+20)
>>> ma.round(masked_x, decimals=1)
masked_array(data=[11.2, -4.0, 0.8, --],
             mask=[False, False, False, True],
    fill_value=1e+20)
>>> ma.round_(masked_x, decimals=-1)
masked_array(data=[10.0, -0.0, 0.0, --],
             mask=[False, False, False, True],
    fill_value=1e+20)
- `right_shift` (ID: bb2e43b6-47a2-4058-8c2b-dae3e1ef390f): Shift the bits of an integer to the right.

This is the masked array version of `numpy.right_shift`, for details
see that function.

See Also
--------
numpy.right_shift

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = [11, 3, 8, 1]
>>> mask = [0, 0, 0, 1]
>>> masked_x = ma.masked_array(x, mask)
>>> masked_x
masked_array(data=[11, 3, 8, --],
             mask=[False, False, False,  True],
       fill_value=999999)
>>> ma.right_shift(masked_x,1)
masked_array(data=[5, 1, 4, --],
             mask=[False, False, False,  True],
       fill_value=999999)
- `resize` (ID: e4abd43c-475d-4082-b3ea-10f35802273c): Return a new masked array with the specified size and shape.

This is the masked equivalent of the `numpy.resize` function. The new
array is filled with repeated copies of `x` (in the order that the
data are stored in memory). If `x` is masked, the new array will be
masked, and the new mask will be a repetition of the old one.

See Also
--------
numpy.resize : Equivalent function in the top level NumPy module.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = ma.array([[1, 2] ,[3, 4]])
>>> a[0, 1] = ma.masked
>>> a
masked_array(
  data=[[1, --],
        [3, 4]],
  mask=[[False,  True],
        [False, False]],
  fill_value=999999)
>>> np.resize(a, (3, 3))
masked_array(
  data=[[1, 2, 3],
        [4, 1, 2],
        [3, 4, 1]],
  mask=False,
  fill_value=999999)
>>> ma.resize(a, (3, 3))
masked_array(
  data=[[1, --, 3],
        [4, 1, --],
        [3, 4, 1]],
  mask=[[False,  True, False],
        [False, False,  True],
        [False, False, False]],
  fill_value=999999)

A MaskedArray is always returned, regardless of the input type.

>>> a = np.array([[1, 2] ,[3, 4]])
>>> ma.resize(a, (3, 3))
masked_array(
  data=[[1, 2, 3],
        [4, 1, 2],
        [3, 4, 1]],
  mask=False,
  fill_value=999999)
- `reshape` (ID: 9f535530-be4c-4d5c-aaf4-d3849109ba9c): Returns an array containing the same data with a new shape.

Refer to `MaskedArray.reshape` for full documentation.

See Also
--------
MaskedArray.reshape : equivalent function

Examples
--------
Reshaping a 1-D array:

>>> a = np.ma.array([1, 2, 3, 4])
>>> np.ma.reshape(a, (2, 2))
masked_array(
  data=[[1, 2],
        [3, 4]],
  mask=False,
  fill_value=999999)

Reshaping a 2-D array:

>>> b = np.ma.array([[1, 2], [3, 4]])
>>> np.ma.reshape(b, (1, 4))
masked_array(data=[[1, 2, 3, 4]],
             mask=False,
       fill_value=999999)

Reshaping a 1-D array with a mask:

>>> c = np.ma.array([1, 2, 3, 4], mask=[False, True, False, False])
>>> np.ma.reshape(c, (2, 2))
masked_array(
  data=[[1, --],
        [3, 4]],
  mask=[[False,  True],
        [False, False]],
  fill_value=999999)
- `putmask` (ID: 7a6aa21e-30d9-421a-8ecd-29ac1abfea75): Changes elements of an array based on conditional and input values.

This is the masked array version of `numpy.putmask`, for details see
`numpy.putmask`.

See Also
--------
numpy.putmask

Notes
-----
Using a masked array as `values` will **not** transform a `ndarray` into
a `MaskedArray`.

Examples
--------
>>> import numpy as np
>>> arr = [[1, 2], [3, 4]]
>>> mask = [[1, 0], [0, 0]]
>>> x = np.ma.array(arr, mask=mask)
>>> np.ma.putmask(x, x < 4, 10*x)
>>> x
masked_array(
  data=[[--, 20],
        [30, 4]],
  mask=[[ True, False],
        [False, False]],
  fill_value=999999)
>>> x.data
array([[10, 20],
       [30,  4]])
- `put` (ID: e2167664-4811-447d-aae8-3347f3208c53): Set storage-indexed locations to corresponding values.

This function is equivalent to `MaskedArray.put`, see that method
for details.

See Also
--------
MaskedArray.put

Examples
--------
Putting values in a masked array:

>>> a = np.ma.array([1, 2, 3, 4], mask=[False, True, False, False])
>>> np.ma.put(a, [1, 3], [10, 30])
>>> a
masked_array(data=[ 1, 10,  3, 30],
             mask=False,
       fill_value=999999)

Using put with a 2D array:

>>> b = np.ma.array([[1, 2], [3, 4]], mask=[[False, True], [False, False]])
>>> np.ma.put(b, [[0, 1], [1, 0]], [[10, 20], [30, 40]])
>>> b
masked_array(
  data=[[40, 30],
        [ 3,  4]],
  mask=False,
  fill_value=999999)
- `ptp` (ID: 78833fdd-779b-4c56-8131-2bf76131785d): No description
- `power` (ID: 639e7401-4385-42ac-844e-8ae3b912aa00): Returns element-wise base array raised to power from second array.

This is the masked array version of `numpy.power`. For details see
`numpy.power`.

See Also
--------
numpy.power

Notes
-----
The *out* argument to `numpy.power` is not supported, `third` has to be
None.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = [11.2, -3.973, 0.801, -1.41]
>>> mask = [0, 0, 0, 1]
>>> masked_x = ma.masked_array(x, mask)
>>> masked_x
masked_array(data=[11.2, -3.973, 0.801, --],
         mask=[False, False, False,  True],
   fill_value=1e+20)
>>> ma.power(masked_x, 2)
masked_array(data=[125.43999999999998, 15.784728999999999,
               0.6416010000000001, --],
         mask=[False, False, False,  True],
   fill_value=1e+20)
>>> y = [-0.5, 2, 0, 17]
>>> masked_y = ma.masked_array(y, mask)
>>> masked_y
masked_array(data=[-0.5, 2.0, 0.0, --],
         mask=[False, False, False,  True],
   fill_value=1e+20)
>>> ma.power(masked_x, masked_y)
masked_array(data=[0.2988071523335984, 15.784728999999999, 1.0, --],
         mask=[False, False, False,  True],
   fill_value=1e+20)
- `outer` (ID: b4d415c3-fd0c-482c-a6fa-48911fe48ee0): maskedarray version of the numpy function.
- `ndim` (ID: 6c002def-f070-472f-8112-a674d7092483): maskedarray version of the numpy function.
- `minimum_fill_value` (ID: b3db2dc4-b62b-4883-89d6-8027ec4eb1ab): Return the maximum value that can be represented by the dtype of an object.

This function is useful for calculating a fill value suitable for
taking the minimum of an array with a given dtype.

Parameters
----------
obj : ndarray, dtype or scalar
    An object that can be queried for it's numeric type.

Returns
-------
val : scalar
    The maximum representable value.

Raises
------
TypeError
    If `obj` isn't a suitable numeric type.

See Also
--------
maximum_fill_value : The inverse function.
set_fill_value : Set the filling value of a masked array.
MaskedArray.fill_value : Return current fill value.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.int8()
>>> ma.minimum_fill_value(a)
127
>>> a = np.int32()
>>> ma.minimum_fill_value(a)
2147483647

An array of numeric data can also be passed.

>>> a = np.array([1, 2, 3], dtype=np.int8)
>>> ma.minimum_fill_value(a)
127
>>> a = np.array([1, 2, 3], dtype=np.float32)
>>> ma.minimum_fill_value(a)
inf
- `min` (ID: 7d2b555a-824f-4cfc-b2d9-9d291e8915f7): No description
- `maximum_fill_value` (ID: a16aca90-f0a6-43e7-b764-8ac1bbc5c09b): Return the minimum value that can be represented by the dtype of an object.

This function is useful for calculating a fill value suitable for
taking the maximum of an array with a given dtype.

Parameters
----------
obj : ndarray, dtype or scalar
    An object that can be queried for it's numeric type.

Returns
-------
val : scalar
    The minimum representable value.

Raises
------
TypeError
    If `obj` isn't a suitable numeric type.

See Also
--------
minimum_fill_value : The inverse function.
set_fill_value : Set the filling value of a masked array.
MaskedArray.fill_value : Return current fill value.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.int8()
>>> ma.maximum_fill_value(a)
-128
>>> a = np.int32()
>>> ma.maximum_fill_value(a)
-2147483648

An array of numeric data can also be passed.

>>> a = np.array([1, 2, 3], dtype=np.int8)
>>> ma.maximum_fill_value(a)
-128
>>> a = np.array([1, 2, 3], dtype=np.float32)
>>> ma.maximum_fill_value(a)
-inf
- `max` (ID: dd5ff5f1-f9a8-49a8-a447-0fd74bf6cdcf): No description
- `masked_where` (ID: 8b1aaae5-4667-4a66-a55b-cddb3b45ace5): Mask an array where a condition is met.

Return `a` as an array masked where `condition` is True.
Any masked values of `a` or `condition` are also masked in the output.

Parameters
----------
condition : array_like
    Masking condition.  When `condition` tests floating point values for
    equality, consider using ``masked_values`` instead.
a : array_like
    Array to mask.
copy : bool
    If True (default) make a copy of `a` in the result.  If False modify
    `a` in place and return a view.

Returns
-------
result : MaskedArray
    The result of masking `a` where `condition` is True.

See Also
--------
masked_values : Mask using floating point equality.
masked_equal : Mask where equal to a given value.
masked_not_equal : Mask where *not* equal to a given value.
masked_less_equal : Mask where less than or equal to a given value.
masked_greater_equal : Mask where greater than or equal to a given value.
masked_less : Mask where less than a given value.
masked_greater : Mask where greater than a given value.
masked_inside : Mask inside a given interval.
masked_outside : Mask outside a given interval.
masked_invalid : Mask invalid values (NaNs or infs).

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_where(a <= 2, a)
masked_array(data=[--, --, --, 3],
             mask=[ True,  True,  True, False],
       fill_value=999999)

Mask array `b` conditional on `a`.

>>> b = ['a', 'b', 'c', 'd']
>>> ma.masked_where(a == 2, b)
masked_array(data=['a', 'b', --, 'd'],
             mask=[False, False,  True, False],
       fill_value='N/A',
            dtype='<U1')

Effect of the `copy` argument.

>>> c = ma.masked_where(a <= 2, a)
>>> c
masked_array(data=[--, --, --, 3],
             mask=[ True,  True,  True, False],
       fill_value=999999)
>>> c[0] = 99
>>> c
masked_array(data=[99, --, --, 3],
             mask=[False,  True,  True, False],
       fill_value=999999)
>>> a
array([0, 1, 2, 3])
>>> c = ma.masked_where(a <= 2, a, copy=False)
>>> c[0] = 99
>>> c
masked_array(data=[99, --, --, 3],
             mask=[False,  True,  True, False],
       fill_value=999999)
>>> a
array([99,  1,  2,  3])

When `condition` or `a` contain masked values.

>>> a = np.arange(4)
>>> a = ma.masked_where(a == 2, a)
>>> a
masked_array(data=[0, 1, --, 3],
             mask=[False, False,  True, False],
       fill_value=999999)
>>> b = np.arange(4)
>>> b = ma.masked_where(b == 0, b)
>>> b
masked_array(data=[--, 1, 2, 3],
             mask=[ True, False, False, False],
       fill_value=999999)
>>> ma.masked_where(a == 3, b)
masked_array(data=[--, 1, --, --],
             mask=[ True, False,  True,  True],
       fill_value=999999)
- `masked_values` (ID: ded684a8-1082-4edc-b4ba-6ad51cf211d7): Mask using floating point equality.

Return a MaskedArray, masked where the data in array `x` are approximately
equal to `value`, determined using `isclose`. The default tolerances for
`masked_values` are the same as those for `isclose`.

For integer types, exact equality is used, in the same way as
`masked_equal`.

The fill_value is set to `value` and the mask is set to ``nomask`` if
possible.

Parameters
----------
x : array_like
    Array to mask.
value : float
    Masking value.
rtol, atol : float, optional
    Tolerance parameters passed on to `isclose`
copy : bool, optional
    Whether to return a copy of `x`.
shrink : bool, optional
    Whether to collapse a mask full of False to ``nomask``.

Returns
-------
result : MaskedArray
    The result of masking `x` where approximately equal to `value`.

See Also
--------
masked_where : Mask where a condition is met.
masked_equal : Mask where equal to a given value (integers).

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = np.array([1, 1.1, 2, 1.1, 3])
>>> ma.masked_values(x, 1.1)
masked_array(data=[1.0, --, 2.0, --, 3.0],
             mask=[False,  True, False,  True, False],
       fill_value=1.1)

Note that `mask` is set to ``nomask`` if possible.

>>> ma.masked_values(x, 2.1)
masked_array(data=[1. , 1.1, 2. , 1.1, 3. ],
             mask=False,
       fill_value=2.1)

Unlike `masked_equal`, `masked_values` can perform approximate equalities.

>>> ma.masked_values(x, 2.1, atol=1e-1)
masked_array(data=[1.0, 1.1, --, 1.1, 3.0],
             mask=[False, False,  True, False, False],
       fill_value=2.1)
- `masked_outside` (ID: c4499205-9ff5-487b-a7e7-5dd19858d467): Mask an array outside a given interval.

Shortcut to ``masked_where``, where `condition` is True for `x` outside
the interval [v1,v2] (x < v1)|(x > v2).
The boundaries `v1` and `v2` can be given in either order.

See Also
--------
masked_where : Mask where a condition is met.

Notes
-----
The array `x` is prefilled with its filling value.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = [0.31, 1.2, 0.01, 0.2, -0.4, -1.1]
>>> ma.masked_outside(x, -0.3, 0.3)
masked_array(data=[--, --, 0.01, 0.2, --, --],
             mask=[ True,  True, False, False,  True,  True],
       fill_value=1e+20)

The order of `v1` and `v2` doesn't matter.

>>> ma.masked_outside(x, 0.3, -0.3)
masked_array(data=[--, --, 0.01, 0.2, --, --],
             mask=[ True,  True, False, False,  True,  True],
       fill_value=1e+20)
- `masked_object` (ID: 13f319ac-5cb1-42b0-80a9-52916d5266f2): Mask the array `x` where the data are exactly equal to value.

This function is similar to `masked_values`, but only suitable
for object arrays: for floating point, use `masked_values` instead.

Parameters
----------
x : array_like
    Array to mask
value : object
    Comparison value
copy : {True, False}, optional
    Whether to return a copy of `x`.
shrink : {True, False}, optional
    Whether to collapse a mask full of False to nomask

Returns
-------
result : MaskedArray
    The result of masking `x` where equal to `value`.

See Also
--------
masked_where : Mask where a condition is met.
masked_equal : Mask where equal to a given value (integers).
masked_values : Mask using floating point equality.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> food = np.array(['green_eggs', 'ham'], dtype=object)
>>> # don't eat spoiled food
>>> eat = ma.masked_object(food, 'green_eggs')
>>> eat
masked_array(data=[--, 'ham'],
             mask=[ True, False],
       fill_value='green_eggs',
            dtype=object)
>>> # plain ol` ham is boring
>>> fresh_food = np.array(['cheese', 'ham', 'pineapple'], dtype=object)
>>> eat = ma.masked_object(fresh_food, 'green_eggs')
>>> eat
masked_array(data=['cheese', 'ham', 'pineapple'],
             mask=False,
       fill_value='green_eggs',
            dtype=object)

Note that `mask` is set to ``nomask`` if possible.

>>> eat
masked_array(data=['cheese', 'ham', 'pineapple'],
             mask=False,
       fill_value='green_eggs',
            dtype=object)
- `masked_not_equal` (ID: 1aa36ef3-46e5-4818-8aea-602415704556): Mask an array where *not* equal to a given value.

This function is a shortcut to ``masked_where``, with
`condition` = (x != value).

See Also
--------
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_not_equal(a, 2)
masked_array(data=[--, --, 2, --],
             mask=[ True,  True, False,  True],
       fill_value=999999)
- `masked_less_equal` (ID: 6d9040b0-8f1f-401f-97cd-363f601256d8): Mask an array where less than or equal to a given value.

This function is a shortcut to ``masked_where``, with
`condition` = (x <= value).

See Also
--------
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_less_equal(a, 2)
masked_array(data=[--, --, --, 3],
             mask=[ True,  True,  True, False],
       fill_value=999999)
- `masked_less` (ID: 07d5c58e-1cda-4c78-8de5-38a82ef03964): Mask an array where less than a given value.

This function is a shortcut to ``masked_where``, with
`condition` = (x < value).

See Also
--------
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_less(a, 2)
masked_array(data=[--, --, 2, 3],
             mask=[ True,  True, False, False],
       fill_value=999999)
- `masked_invalid` (ID: 3a8b802d-3d32-486a-8d34-7dc9cee4cc59): Mask an array where invalid values occur (NaNs or infs).

This function is a shortcut to ``masked_where``, with
`condition` = ~(np.isfinite(a)). Any pre-existing mask is conserved.
Only applies to arrays with a dtype where NaNs or infs make sense
(i.e. floating point types), but accepts any array_like object.

See Also
--------
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(5, dtype=float)
>>> a[2] = np.nan
>>> a[3] = np.inf
>>> a
array([ 0.,  1., nan, inf,  4.])
>>> ma.masked_invalid(a)
masked_array(data=[0.0, 1.0, --, --, 4.0],
             mask=[False, False,  True,  True, False],
       fill_value=1e+20)
- `masked_inside` (ID: 6c04568b-c832-4b6f-a22e-ea25cdab35ae): Mask an array inside a given interval.

Shortcut to ``masked_where``, where `condition` is True for `x` inside
the interval [v1,v2] (v1 <= x <= v2).  The boundaries `v1` and `v2`
can be given in either order.

See Also
--------
masked_where : Mask where a condition is met.

Notes
-----
The array `x` is prefilled with its filling value.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = [0.31, 1.2, 0.01, 0.2, -0.4, -1.1]
>>> ma.masked_inside(x, -0.3, 0.3)
masked_array(data=[0.31, 1.2, --, --, -0.4, -1.1],
             mask=[False, False,  True,  True, False, False],
       fill_value=1e+20)

The order of `v1` and `v2` doesn't matter.

>>> ma.masked_inside(x, 0.3, -0.3)
masked_array(data=[0.31, 1.2, --, --, -0.4, -1.1],
             mask=[False, False,  True,  True, False, False],
       fill_value=1e+20)
- `masked_greater_equal` (ID: 46e23876-c8b6-4be0-868e-8ab0050f9b22): Mask an array where greater than or equal to a given value.

This function is a shortcut to ``masked_where``, with
`condition` = (x >= value).

See Also
--------
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_greater_equal(a, 2)
masked_array(data=[0, 1, --, --],
             mask=[False, False,  True,  True],
       fill_value=999999)
- `masked_greater` (ID: 9bab1cbf-5ef2-43f0-a549-88cbbc37b448): Mask an array where greater than a given value.

This function is a shortcut to ``masked_where``, with
`condition` = (x > value).

See Also
--------
masked_where : Mask where a condition is met.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_greater(a, 2)
masked_array(data=[0, 1, 2, --],
             mask=[False, False, False,  True],
       fill_value=999999)
- `masked_equal` (ID: 822c0052-e343-4089-b91b-e845deaf586e): Mask an array where equal to a given value.

Return a MaskedArray, masked where the data in array `x` are
equal to `value`. The fill_value of the returned MaskedArray
is set to `value`.

For floating point arrays, consider using ``masked_values(x, value)``.

See Also
--------
masked_where : Mask where a condition is met.
masked_values : Mask using floating point equality.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> ma.masked_equal(a, 2)
masked_array(data=[0, 1, --, 3],
             mask=[False, False,  True, False],
       fill_value=2)
- `mask_or` (ID: bd451ea3-57bd-40bd-9989-ad39ee2efdd7): Combine two masks with the ``logical_or`` operator.

The result may be a view on `m1` or `m2` if the other is `nomask`
(i.e. False).

Parameters
----------
m1, m2 : array_like
    Input masks.
copy : bool, optional
    If copy is False and one of the inputs is `nomask`, return a view
    of the other input mask. Defaults to False.
shrink : bool, optional
    Whether to shrink the output to `nomask` if all its values are
    False. Defaults to True.

Returns
-------
mask : output mask
    The result masks values that are masked in either `m1` or `m2`.

Raises
------
ValueError
    If `m1` and `m2` have different flexible dtypes.

Examples
--------
>>> import numpy as np
>>> m1 = np.ma.make_mask([0, 1, 1, 0])
>>> m2 = np.ma.make_mask([1, 0, 0, 0])
>>> np.ma.mask_or(m1, m2)
array([ True,  True,  True, False])
- `make_mask_none` (ID: 6587f765-5958-4ef2-bbc8-278f6cb5481f): Return a boolean mask of the given shape, filled with False.

This function returns a boolean ndarray with all entries False, that can
be used in common mask manipulations. If a complex dtype is specified, the
type of each field is converted to a boolean type.

Parameters
----------
newshape : tuple
    A tuple indicating the shape of the mask.
dtype : {None, dtype}, optional
    If None, use a MaskType instance. Otherwise, use a new datatype with
    the same fields as `dtype`, converted to boolean types.

Returns
-------
result : ndarray
    An ndarray of appropriate shape and dtype, filled with False.

See Also
--------
make_mask : Create a boolean mask from an array.
make_mask_descr : Construct a dtype description list from a given dtype.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> ma.make_mask_none((3,))
array([False, False, False])

Defining a more complex dtype.

>>> dtype = np.dtype({'names':['foo', 'bar'],
...                   'formats':[np.float32, np.int64]})
>>> dtype
dtype([('foo', '<f4'), ('bar', '<i8')])
>>> ma.make_mask_none((3,), dtype=dtype)
array([(False, False), (False, False), (False, False)],
      dtype=[('foo', '|b1'), ('bar', '|b1')])
- `make_mask_descr` (ID: d0ac9cf5-a11e-431d-85d4-62b7a767a4bd): Construct a dtype description list from a given dtype.

Returns a new dtype object, with the type of all fields in `ndtype` to a
boolean type. Field names are not altered.

Parameters
----------
ndtype : dtype
    The dtype to convert.

Returns
-------
result : dtype
    A dtype that looks like `ndtype`, the type of all fields is boolean.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> dtype = np.dtype({'names':['foo', 'bar'],
...                   'formats':[np.float32, np.int64]})
>>> dtype
dtype([('foo', '<f4'), ('bar', '<i8')])
>>> ma.make_mask_descr(dtype)
dtype([('foo', '|b1'), ('bar', '|b1')])
>>> ma.make_mask_descr(np.float32)
dtype('bool')
- `make_mask` (ID: 51828a30-46c5-4889-b3ab-505283bb33ed): Create a boolean mask from an array.

Return `m` as a boolean mask, creating a copy if necessary or requested.
The function can accept any sequence that is convertible to integers,
or ``nomask``.  Does not require that contents must be 0s and 1s, values
of 0 are interpreted as False, everything else as True.

Parameters
----------
m : array_like
    Potential mask.
copy : bool, optional
    Whether to return a copy of `m` (True) or `m` itself (False).
shrink : bool, optional
    Whether to shrink `m` to ``nomask`` if all its values are False.
dtype : dtype, optional
    Data-type of the output mask. By default, the output mask has a
    dtype of MaskType (bool). If the dtype is flexible, each field has
    a boolean dtype. This is ignored when `m` is ``nomask``, in which
    case ``nomask`` is always returned.

Returns
-------
result : ndarray
    A boolean mask derived from `m`.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> m = [True, False, True, True]
>>> ma.make_mask(m)
array([ True, False,  True,  True])
>>> m = [1, 0, 1, 1]
>>> ma.make_mask(m)
array([ True, False,  True,  True])
>>> m = [1, 0, 2, -3]
>>> ma.make_mask(m)
array([ True, False,  True,  True])

Effect of the `shrink` parameter.

>>> m = np.zeros(4)
>>> m
array([0., 0., 0., 0.])
>>> ma.make_mask(m)
False
>>> ma.make_mask(m, shrink=False)
array([False, False, False, False])

Using a flexible `dtype`.

>>> m = [1, 0, 1, 1]
>>> n = [0, 1, 0, 0]
>>> arr = []
>>> for man, mouse in zip(m, n):
...     arr.append((man, mouse))
>>> arr
[(1, 0), (0, 1), (1, 0), (1, 0)]
>>> dtype = np.dtype({'names':['man', 'mouse'],
...                   'formats':[np.int64, np.int64]})
>>> arr = np.array(arr, dtype=dtype)
>>> arr
array([(1, 0), (0, 1), (1, 0), (1, 0)],
      dtype=[('man', '<i8'), ('mouse', '<i8')])
>>> ma.make_mask(arr, dtype=dtype)
array([(True, False), (False, True), (True, False), (True, False)],
      dtype=[('man', '|b1'), ('mouse', '|b1')])
- `left_shift` (ID: 8091516d-1cec-40b4-a5f8-f8c63a526081): Shift the bits of an integer to the left.

This is the masked array version of `numpy.left_shift`, for details
see that function.

See Also
--------
numpy.left_shift

Examples
--------
Shift with a masked array:

>>> arr = np.ma.array([10, 20, 30], mask=[False, True, False])
>>> np.ma.left_shift(arr, 1)
masked_array(data=[20, --, 60],
             mask=[False,  True, False],
       fill_value=999999)

Large shift:

>>> np.ma.left_shift(10, 10)
masked_array(data=10240,
             mask=False,
       fill_value=999999)

Shift with a scalar and an array:

>>> scalar = 10
>>> arr = np.ma.array([1, 2, 3], mask=[False, True, False])
>>> np.ma.left_shift(scalar, arr)
masked_array(data=[20, --, 80],
             mask=[False,  True, False],
       fill_value=999999)
- `is_masked` (ID: 6e788322-7972-47be-9e49-f193bd5eb903): Determine whether input has masked values.

Accepts any object as input, but always returns False unless the
input is a MaskedArray containing masked values.

Parameters
----------
x : array_like
    Array to check for masked values.

Returns
-------
result : bool
    True if `x` is a MaskedArray with masked values, False otherwise.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = ma.masked_equal([0, 1, 0, 2, 3], 0)
>>> x
masked_array(data=[--, 1, --, 2, 3],
             mask=[ True, False,  True, False, False],
       fill_value=0)
>>> ma.is_masked(x)
True
>>> x = ma.masked_equal([0, 1, 0, 2, 3], 42)
>>> x
masked_array(data=[0, 1, 0, 2, 3],
             mask=False,
       fill_value=42)
>>> ma.is_masked(x)
False

Always returns False if `x` isn't a MaskedArray.

>>> x = [False, True, False]
>>> ma.is_masked(x)
False
>>> x = 'a string'
>>> ma.is_masked(x)
False
- `is_mask` (ID: a0283b92-f111-4094-9653-4ff67839da59): Return True if m is a valid, standard mask.

This function does not check the contents of the input, only that the
type is MaskType. In particular, this function returns False if the
mask has a flexible dtype.

Parameters
----------
m : array_like
    Array to test.

Returns
-------
result : bool
    True if `m.dtype.type` is MaskType, False otherwise.

See Also
--------
ma.isMaskedArray : Test whether input is an instance of MaskedArray.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> m = ma.masked_equal([0, 1, 0, 2, 3], 0)
>>> m
masked_array(data=[--, 1, --, 2, 3],
             mask=[ True, False,  True, False, False],
       fill_value=0)
>>> ma.is_mask(m)
False
>>> ma.is_mask(m.mask)
True

Input must be an ndarray (or have similar attributes)
for it to be considered a valid mask.

>>> m = [False, True, False]
>>> ma.is_mask(m)
False
>>> m = np.array([False, True, False])
>>> m
array([False,  True, False])
>>> ma.is_mask(m)
True

Arrays with complex dtypes don't return True.

>>> dtype = np.dtype({'names':['monty', 'pithon'],
...                   'formats':[bool, bool]})
>>> dtype
dtype([('monty', '|b1'), ('pithon', '|b1')])
>>> m = np.array([(True, False), (False, True), (True, False)],
...              dtype=dtype)
>>> m
array([( True, False), (False,  True), ( True, False)],
      dtype=[('monty', '?'), ('pithon', '?')])
>>> ma.is_mask(m)
False
- `isMaskedArray` (ID: 5ceb67bb-576a-4b54-9c45-a30740bcbc1a): Test whether input is an instance of MaskedArray.

This function returns True if `x` is an instance of MaskedArray
and returns False otherwise.  Any object is accepted as input.

Parameters
----------
x : object
    Object to test.

Returns
-------
result : bool
    True if `x` is a MaskedArray.

See Also
--------
isMA : Alias to isMaskedArray.
isarray : Alias to isMaskedArray.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = np.eye(3, 3)
>>> a
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
>>> m = ma.masked_values(a, 0)
>>> m
masked_array(
  data=[[1.0, --, --],
        [--, 1.0, --],
        [--, --, 1.0]],
  mask=[[False,  True,  True],
        [ True, False,  True],
        [ True,  True, False]],
  fill_value=0.0)
>>> ma.isMaskedArray(a)
False
>>> ma.isMaskedArray(m)
True
>>> ma.isMaskedArray([0, 1, 2])
False
- `inner` (ID: 263d585f-4b12-4d19-b90a-120d1ae08229): Returns the inner product of a and b for arrays of floating point types.

Like the generic NumPy equivalent the product sum is over the last dimension
of a and b. The first argument is not conjugated.
- `getmaskarray` (ID: 08e1312b-31fc-4909-a07e-d55d7e4ff81c): Return the mask of a masked array, or full boolean array of False.

Return the mask of `arr` as an ndarray if `arr` is a `MaskedArray` and
the mask is not `nomask`, else return a full boolean array of False of
the same shape as `arr`.

Parameters
----------
arr : array_like
    Input `MaskedArray` for which the mask is required.

See Also
--------
getmask : Return the mask of a masked array, or nomask.
getdata : Return the data of a masked array as an ndarray.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = ma.masked_equal([[1,2],[3,4]], 2)
>>> a
masked_array(
  data=[[1, --],
        [3, 4]],
  mask=[[False,  True],
        [False, False]],
  fill_value=2)
>>> ma.getmaskarray(a)
array([[False,  True],
       [False, False]])

Result when mask == ``nomask``

>>> b = ma.masked_array([[1,2],[3,4]])
>>> b
masked_array(
  data=[[1, 2],
        [3, 4]],
  mask=False,
  fill_value=999999)
>>> ma.getmaskarray(b)
array([[False, False],
       [False, False]])
- `getmask` (ID: 119893be-171d-41c7-8d56-a5c9200e4cbb): Return the mask of a masked array, or nomask.

Return the mask of `a` as an ndarray if `a` is a `MaskedArray` and the
mask is not `nomask`, else return `nomask`. To guarantee a full array
of booleans of the same shape as a, use `getmaskarray`.

Parameters
----------
a : array_like
    Input `MaskedArray` for which the mask is required.

See Also
--------
getdata : Return the data of a masked array as an ndarray.
getmaskarray : Return the mask of a masked array, or full array of False.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = ma.masked_equal([[1,2],[3,4]], 2)
>>> a
masked_array(
  data=[[1, --],
        [3, 4]],
  mask=[[False,  True],
        [False, False]],
  fill_value=2)
>>> ma.getmask(a)
array([[False,  True],
       [False, False]])

Equivalently use the `MaskedArray` `mask` attribute.

>>> a.mask
array([[False,  True],
       [False, False]])

Result when mask == `nomask`

>>> b = ma.masked_array([[1,2],[3,4]])
>>> b
masked_array(
  data=[[1, 2],
        [3, 4]],
  mask=False,
  fill_value=999999)
>>> ma.nomask
False
>>> ma.getmask(b) == ma.nomask
True
>>> b.mask == ma.nomask
True
- `getdata` (ID: 419c70be-b2e1-4f3f-b8d7-ac55e2165b71): Return the data of a masked array as an ndarray.

Return the data of `a` (if any) as an ndarray if `a` is a ``MaskedArray``,
else return `a` as a ndarray or subclass (depending on `subok`) if not.

Parameters
----------
a : array_like
    Input ``MaskedArray``, alternatively a ndarray or a subclass thereof.
subok : bool
    Whether to force the output to be a `pure` ndarray (False) or to
    return a subclass of ndarray if appropriate (True, default).

See Also
--------
getmask : Return the mask of a masked array, or nomask.
getmaskarray : Return the mask of a masked array, or full array of False.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = ma.masked_equal([[1,2],[3,4]], 2)
>>> a
masked_array(
  data=[[1, --],
        [3, 4]],
  mask=[[False,  True],
        [False, False]],
  fill_value=2)
>>> ma.getdata(a)
array([[1, 2],
       [3, 4]])

Equivalently use the ``MaskedArray`` `data` attribute.

>>> a.data
array([[1, 2],
       [3, 4]])
- `fromflex` (ID: 55525186-7e7b-4932-926d-05f1160c1eb4): Build a masked array from a suitable flexible-type array.

The input array has to have a data-type with ``_data`` and ``_mask``
fields. This type of array is output by `MaskedArray.toflex`.

Parameters
----------
fxarray : ndarray
    The structured input array, containing ``_data`` and ``_mask``
    fields. If present, other fields are discarded.

Returns
-------
result : MaskedArray
    The constructed masked array.

See Also
--------
MaskedArray.toflex : Build a flexible-type array from a masked array.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array(np.arange(9).reshape(3, 3), mask=[0] + [1, 0] * 4)
>>> rec = x.toflex()
>>> rec
array([[(0, False), (1,  True), (2, False)],
       [(3,  True), (4, False), (5,  True)],
       [(6, False), (7,  True), (8, False)]],
      dtype=[('_data', '<i8'), ('_mask', '?')])
>>> x2 = np.ma.fromflex(rec)
>>> x2
masked_array(
  data=[[0, --, 2],
        [--, 4, --],
        [6, --, 8]],
  mask=[[False,  True, False],
        [ True, False,  True],
        [False,  True, False]],
  fill_value=999999)

Extra fields can be present in the structured array but are discarded:

>>> dt = [('_data', '<i4'), ('_mask', '|b1'), ('field3', '<f4')]
>>> rec2 = np.zeros((2, 2), dtype=dt)
>>> rec2
array([[(0, False, 0.), (0, False, 0.)],
       [(0, False, 0.), (0, False, 0.)]],
      dtype=[('_data', '<i4'), ('_mask', '?'), ('field3', '<f4')])
>>> y = np.ma.fromflex(rec2)
>>> y
masked_array(
  data=[[0, 0],
        [0, 0]],
  mask=[[False, False],
        [False, False]],
  fill_value=np.int64(999999),
  dtype=int32)
- `flatten_structured_array` (ID: 64c196c6-6748-48bd-8587-b09f85e8dbac): Flatten a structured array.

The data type of the output is chosen such that it can represent all of the
(nested) fields.

Parameters
----------
a : structured array

Returns
-------
output : masked array or ndarray
    A flattened masked array if the input is a masked array, otherwise a
    standard ndarray.

Examples
--------
>>> import numpy as np
>>> ndtype = [('a', int), ('b', float)]
>>> a = np.array([(1, 1), (2, 2)], dtype=ndtype)
>>> np.ma.flatten_structured_array(a)
array([[1., 1.],
       [2., 2.]])
- `flatten_mask` (ID: 08327915-ec9b-40ce-b16b-845cc30fdbd6): Returns a completely flattened version of the mask, where nested fields
are collapsed.

Parameters
----------
mask : array_like
    Input array, which will be interpreted as booleans.

Returns
-------
flattened_mask : ndarray of bools
    The flattened input.

Examples
--------
>>> import numpy as np
>>> mask = np.array([0, 0, 1])
>>> np.ma.flatten_mask(mask)
array([False, False,  True])

>>> mask = np.array([(0, 0), (0, 1)], dtype=[('a', bool), ('b', bool)])
>>> np.ma.flatten_mask(mask)
array([False, False, False,  True])

>>> mdtype = [('a', bool), ('b', [('ba', bool), ('bb', bool)])]
>>> mask = np.array([(0, (0, 0)), (0, (0, 1))], dtype=mdtype)
>>> np.ma.flatten_mask(mask)
array([False, False, False, False, False,  True])
- `fix_invalid` (ID: 7061001e-4382-4b17-8a19-f3ead252dc58): Return input with invalid data masked and replaced by a fill value.

Invalid data means values of `nan`, `inf`, etc.

Parameters
----------
a : array_like
    Input array, a (subclass of) ndarray.
mask : sequence, optional
    Mask. Must be convertible to an array of booleans with the same
    shape as `data`. True indicates a masked (i.e. invalid) data.
copy : bool, optional
    Whether to use a copy of `a` (True) or to fix `a` in place (False).
    Default is True.
fill_value : scalar, optional
    Value used for fixing invalid data. Default is None, in which case
    the ``a.fill_value`` is used.

Returns
-------
b : MaskedArray
    The input array with invalid entries fixed.

Notes
-----
A copy is performed by default.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array([1., -1, np.nan, np.inf], mask=[1] + [0]*3)
>>> x
masked_array(data=[--, -1.0, nan, inf],
             mask=[ True, False, False, False],
       fill_value=1e+20)
>>> np.ma.fix_invalid(x)
masked_array(data=[--, -1.0, --, --],
             mask=[ True, False,  True,  True],
       fill_value=1e+20)

>>> fixed = np.ma.fix_invalid(x)
>>> fixed.data
array([ 1.e+00, -1.e+00,  1.e+20,  1.e+20])
>>> x.data
array([ 1., -1., nan, inf])
- `filled` (ID: 2266ca79-8533-4de9-a0ce-f9485a1575b6): Return input as an `~numpy.ndarray`, with masked values replaced by
`fill_value`.

If `a` is not a `MaskedArray`, `a` itself is returned.
If `a` is a `MaskedArray` with no masked values, then ``a.data`` is
returned.
If `a` is a `MaskedArray` and `fill_value` is None, `fill_value` is set to
``a.fill_value``.

Parameters
----------
a : MaskedArray or array_like
    An input object.
fill_value : array_like, optional.
    Can be scalar or non-scalar. If non-scalar, the
    resulting filled array should be broadcastable
    over input array. Default is None.

Returns
-------
a : ndarray
    The filled array.

See Also
--------
compressed

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
...                                                [1, 0, 0],
...                                                [0, 0, 0]])
>>> x.filled()
array([[999999,      1,      2],
       [999999,      4,      5],
       [     6,      7,      8]])
>>> x.filled(fill_value=333)
array([[333,   1,   2],
       [333,   4,   5],
       [  6,   7,   8]])
>>> x.filled(fill_value=np.arange(3))
array([[0, 1, 2],
       [0, 4, 5],
       [6, 7, 8]])
- `diff` (ID: 67179c6f-31c0-40b6-b8b7-37650e8dde85): Calculate the n-th discrete difference along the given axis.
The first difference is given by ``out[i] = a[i+1] - a[i]`` along
the given axis, higher differences are calculated by using `diff`
recursively.
Preserves the input mask.

Parameters
----------
a : array_like
    Input array
n : int, optional
    The number of times values are differenced. If zero, the input
    is returned as-is.
axis : int, optional
    The axis along which the difference is taken, default is the
    last axis.
prepend, append : array_like, optional
    Values to prepend or append to `a` along axis prior to
    performing the difference.  Scalar values are expanded to
    arrays with length 1 in the direction of axis and the shape
    of the input array in along all other axes.  Otherwise the
    dimension and shape must match `a` except along axis.

Returns
-------
diff : MaskedArray
    The n-th differences. The shape of the output is the same as `a`
    except along `axis` where the dimension is smaller by `n`. The
    type of the output is the same as the type of the difference
    between any two elements of `a`. This is the same as the type of
    `a` in most cases. A notable exception is `datetime64`, which
    results in a `timedelta64` output array.

See Also
--------
numpy.diff : Equivalent function in the top-level NumPy module.

Notes
-----
Type is preserved for boolean arrays, so the result will contain
`False` when consecutive elements are the same and `True` when they
differ.

For unsigned integer arrays, the results will also be unsigned. This
should not be surprising, as the result is consistent with
calculating the difference directly:

>>> u8_arr = np.array([1, 0], dtype=np.uint8)
>>> np.ma.diff(u8_arr)
masked_array(data=[255],
             mask=False,
       fill_value=np.uint64(999999),
            dtype=uint8)
>>> u8_arr[1,...] - u8_arr[0,...]
np.uint8(255)

If this is not desirable, then the array should be cast to a larger
integer type first:

>>> i16_arr = u8_arr.astype(np.int16)
>>> np.ma.diff(i16_arr)
masked_array(data=[-1],
             mask=False,
       fill_value=np.int64(999999),
            dtype=int16)

Examples
--------
>>> import numpy as np
>>> a = np.array([1, 2, 3, 4, 7, 0, 2, 3])
>>> x = np.ma.masked_where(a < 2, a)
>>> np.ma.diff(x)
masked_array(data=[--, 1, 1, 3, --, --, 1],
        mask=[ True, False, False, False,  True,  True, False],
    fill_value=999999)

>>> np.ma.diff(x, n=2)
masked_array(data=[--, 0, 2, --, --, --],
            mask=[ True, False, False,  True,  True,  True],
    fill_value=999999)

>>> a = np.array([[1, 3, 1, 5, 10], [0, 1, 5, 6, 8]])
>>> x = np.ma.masked_equal(a, value=1)
>>> np.ma.diff(x)
masked_array(
    data=[[--, --, --, 5],
            [--, --, 1, 2]],
    mask=[[ True,  True,  True, False],
            [ True,  True, False, False]],
    fill_value=1)

>>> np.ma.diff(x, axis=0)
masked_array(data=[[--, --, --, 1, -2]],
        mask=[[ True,  True,  True, False, False]],
    fill_value=1)
- `diag` (ID: 0380d2ed-c565-479a-9c32-803afa8d9f08): Extract a diagonal or construct a diagonal array.

This function is the equivalent of `numpy.diag` that takes masked
values into account, see `numpy.diag` for details.

See Also
--------
numpy.diag : Equivalent function for ndarrays.

Examples
--------
>>> import numpy as np

Create an array with negative values masked:

>>> import numpy as np
>>> x = np.array([[11.2, -3.973, 18], [0.801, -1.41, 12], [7, 33, -12]])
>>> masked_x = np.ma.masked_array(x, mask=x < 0)
>>> masked_x
masked_array(
  data=[[11.2, --, 18.0],
        [0.801, --, 12.0],
        [7.0, 33.0, --]],
  mask=[[False,  True, False],
        [False,  True, False],
        [False, False,  True]],
  fill_value=1e+20)

Isolate the main diagonal from the masked array:

>>> np.ma.diag(masked_x)
masked_array(data=[11.2, --, --],
             mask=[False,  True,  True],
       fill_value=1e+20)

Isolate the first diagonal below the main diagonal:

>>> np.ma.diag(masked_x, -1)
masked_array(data=[0.801, 33.0],
             mask=[False, False],
       fill_value=1e+20)
- `default_fill_value` (ID: a7284a07-901a-4ef7-ad36-e1756ddfb70e): Return the default fill value for the argument object.

The default filling value depends on the datatype of the input
array or the type of the input scalar:

   ========  ========
   datatype  default
   ========  ========
   bool      True
   int       999999
   float     1.e20
   complex   1.e20+0j
   object    '?'
   string    'N/A'
   ========  ========

For structured types, a structured scalar is returned, with each field the
default fill value for its type.

For subarray types, the fill value is an array of the same size containing
the default scalar fill value.

Parameters
----------
obj : ndarray, dtype or scalar
    The array data-type or scalar for which the default fill value
    is returned.

Returns
-------
fill_value : scalar
    The default fill value.

Examples
--------
>>> import numpy as np
>>> np.ma.default_fill_value(1)
999999
>>> np.ma.default_fill_value(np.array([1.1, 2., np.pi]))
1e+20
>>> np.ma.default_fill_value(np.dtype(complex))
(1e+20+0j)
- `correlate` (ID: b548c653-7ab5-400b-a449-b62c4fb13c36): Cross-correlation of two 1-dimensional sequences.

Parameters
----------
a, v : array_like
    Input sequences.
mode : {'valid', 'same', 'full'}, optional
    Refer to the `np.convolve` docstring.  Note that the default
    is 'valid', unlike `convolve`, which uses 'full'.
propagate_mask : bool
    If True, then a result element is masked if any masked element contributes
    towards it. If False, then a result element is only masked if no non-masked
    element contribute towards it

Returns
-------
out : MaskedArray
    Discrete cross-correlation of `a` and `v`.

See Also
--------
numpy.correlate : Equivalent function in the top-level NumPy module.

Examples
--------
Basic correlation:

>>> a = np.ma.array([1, 2, 3])
>>> v = np.ma.array([0, 1, 0])
>>> np.ma.correlate(a, v, mode='valid')
masked_array(data=[2],
             mask=[False],
       fill_value=999999)

Correlation with masked elements:

>>> a = np.ma.array([1, 2, 3], mask=[False, True, False])
>>> v = np.ma.array([0, 1, 0])
>>> np.ma.correlate(a, v, mode='valid', propagate_mask=True)
masked_array(data=[--],
             mask=[ True],
       fill_value=999999,
            dtype=int64)

Correlation with different modes and mixed array types:

>>> a = np.ma.array([1, 2, 3])
>>> v = np.ma.array([0, 1, 0])
>>> np.ma.correlate(a, v, mode='full')
masked_array(data=[0, 1, 2, 3, 0],
             mask=[False, False, False, False, False],
       fill_value=999999)
- `convolve` (ID: b90ff26e-f29a-494f-a94c-5e0296d17277): Returns the discrete, linear convolution of two one-dimensional sequences.

Parameters
----------
a, v : array_like
    Input sequences.
mode : {'valid', 'same', 'full'}, optional
    Refer to the `np.convolve` docstring.
propagate_mask : bool
    If True, then if any masked element is included in the sum for a result
    element, then the result is masked.
    If False, then the result element is only masked if no non-masked cells
    contribute towards it

Returns
-------
out : MaskedArray
    Discrete, linear convolution of `a` and `v`.

See Also
--------
numpy.convolve : Equivalent function in the top-level NumPy module.
- `concatenate` (ID: 00ad9c04-9bce-49c5-9a23-a96215ec4f9e): Concatenate a sequence of arrays along the given axis.

Parameters
----------
arrays : sequence of array_like
    The arrays must have the same shape, except in the dimension
    corresponding to `axis` (the first, by default).
axis : int, optional
    The axis along which the arrays will be joined. Default is 0.

Returns
-------
result : MaskedArray
    The concatenated array with any masked entries preserved.

See Also
--------
numpy.concatenate : Equivalent function in the top-level NumPy module.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = ma.arange(3)
>>> a[1] = ma.masked
>>> b = ma.arange(2, 5)
>>> a
masked_array(data=[0, --, 2],
             mask=[False,  True, False],
       fill_value=999999)
>>> b
masked_array(data=[2, 3, 4],
             mask=False,
       fill_value=999999)
>>> ma.concatenate([a, b])
masked_array(data=[0, --, 2, 2, 3, 4],
             mask=[False,  True, False, False, False, False],
       fill_value=999999)
- `compressed` (ID: efabc3b7-77ba-4e89-afdf-54aa417d6b64): Return all the non-masked data as a 1-D array.

This function is equivalent to calling the "compressed" method of a
`ma.MaskedArray`, see `ma.MaskedArray.compressed` for details.

See Also
--------
ma.MaskedArray.compressed : Equivalent method.

Examples
--------
>>> import numpy as np

Create an array with negative values masked:

>>> import numpy as np
>>> x = np.array([[1, -1, 0], [2, -1, 3], [7, 4, -1]])
>>> masked_x = np.ma.masked_array(x, mask=x < 0)
>>> masked_x
masked_array(
  data=[[1, --, 0],
        [2, --, 3],
        [7, 4, --]],
  mask=[[False,  True, False],
        [False,  True, False],
        [False, False,  True]],
  fill_value=999999)

Compress the masked array into a 1-D array of non-masked values:

>>> np.ma.compressed(masked_x)
array([1, 0, 2, 3, 7, 4])
- `common_fill_value` (ID: 9dd0c6b5-8d89-4779-8949-5ef61834b9ed): Return the common filling value of two masked arrays, if any.

If ``a.fill_value == b.fill_value``, return the fill value,
otherwise return None.

Parameters
----------
a, b : MaskedArray
    The masked arrays for which to compare fill values.

Returns
-------
fill_value : scalar or None
    The common fill value, or None.

Examples
--------
>>> import numpy as np
>>> x = np.ma.array([0, 1.], fill_value=3)
>>> y = np.ma.array([0, 1.], fill_value=3)
>>> np.ma.common_fill_value(x, y)
3.0
- `choose` (ID: c6af1915-ce36-468d-be86-f39ba6dc9224): Use an index array to construct a new array from a list of choices.

Given an array of integers and a list of n choice arrays, this method
will create a new array that merges each of the choice arrays.  Where a
value in `index` is i, the new array will have the value that choices[i]
contains in the same place.

Parameters
----------
indices : ndarray of ints
    This array must contain integers in ``[0, n-1]``, where n is the
    number of choices.
choices : sequence of arrays
    Choice arrays. The index array and all of the choices should be
    broadcastable to the same shape.
out : array, optional
    If provided, the result will be inserted into this array. It should
    be of the appropriate shape and `dtype`.
mode : {'raise', 'wrap', 'clip'}, optional
    Specifies how out-of-bounds indices will behave.

    * 'raise' : raise an error
    * 'wrap' : wrap around
    * 'clip' : clip to the range

Returns
-------
merged_array : array

See Also
--------
choose : equivalent function

Examples
--------
>>> import numpy as np
>>> choice = np.array([[1,1,1], [2,2,2], [3,3,3]])
>>> a = np.array([2, 1, 0])
>>> np.ma.choose(a, choice)
masked_array(data=[3, 2, 1],
             mask=False,
       fill_value=999999)
- `asarray` (ID: ad215e78-37a3-47e0-9e53-95d22d35b731): Convert the input to a masked array of the given data-type.

No copy is performed if the input is already an `ndarray`. If `a` is
a subclass of `MaskedArray`, a base class `MaskedArray` is returned.

Parameters
----------
a : array_like
    Input data, in any form that can be converted to a masked array. This
    includes lists, lists of tuples, tuples, tuples of tuples, tuples
    of lists, ndarrays and masked arrays.
dtype : dtype, optional
    By default, the data-type is inferred from the input data.
order : {'C', 'F'}, optional
    Whether to use row-major ('C') or column-major ('FORTRAN') memory
    representation.  Default is 'C'.

Returns
-------
out : MaskedArray
    Masked array interpretation of `a`.

See Also
--------
asanyarray : Similar to `asarray`, but conserves subclasses.

Examples
--------
>>> import numpy as np
>>> x = np.arange(10.).reshape(2, 5)
>>> x
array([[0., 1., 2., 3., 4.],
       [5., 6., 7., 8., 9.]])
>>> np.ma.asarray(x)
masked_array(
  data=[[0., 1., 2., 3., 4.],
        [5., 6., 7., 8., 9.]],
  mask=False,
  fill_value=1e+20)
>>> type(np.ma.asarray(x))
<class 'numpy.ma.MaskedArray'>
- `asanyarray` (ID: 6eafcef8-96df-4557-8da4-37ce5838ad7e): Convert the input to a masked array, conserving subclasses.

If `a` is a subclass of `MaskedArray`, its class is conserved.
No copy is performed if the input is already an `ndarray`.

Parameters
----------
a : array_like
    Input data, in any form that can be converted to an array.
dtype : dtype, optional
    By default, the data-type is inferred from the input data.
order : {'C', 'F'}, optional
    Whether to use row-major ('C') or column-major ('FORTRAN') memory
    representation.  Default is 'C'.

Returns
-------
out : MaskedArray
    MaskedArray interpretation of `a`.

See Also
--------
asarray : Similar to `asanyarray`, but does not conserve subclass.

Examples
--------
>>> import numpy as np
>>> x = np.arange(10.).reshape(2, 5)
>>> x
array([[0., 1., 2., 3., 4.],
       [5., 6., 7., 8., 9.]])
>>> np.ma.asanyarray(x)
masked_array(
  data=[[0., 1., 2., 3., 4.],
        [5., 6., 7., 8., 9.]],
  mask=False,
  fill_value=1e+20)
>>> type(np.ma.asanyarray(x))
<class 'numpy.ma.MaskedArray'>
- `array` (ID: 590bd85a-e3c8-4e1f-b47a-ba831d152cbd): Shortcut to MaskedArray.

The options are in a different order for convenience and backwards
compatibility.
- `argsort` (ID: 7ca2b491-5113-40ac-907d-308469cf39fa): Function version of the eponymous method.
- `append` (ID: 55083cf0-4f20-42e1-874c-2667dd80a5f1): Append values to the end of an array.

Parameters
----------
a : array_like
    Values are appended to a copy of this array.
b : array_like
    These values are appended to a copy of `a`.  It must be of the
    correct shape (the same shape as `a`, excluding `axis`).  If `axis`
    is not specified, `b` can be any shape and will be flattened
    before use.
axis : int, optional
    The axis along which `v` are appended.  If `axis` is not given,
    both `a` and `b` are flattened before use.

Returns
-------
append : MaskedArray
    A copy of `a` with `b` appended to `axis`.  Note that `append`
    does not occur in-place: a new array is allocated and filled.  If
    `axis` is None, the result is a flattened array.

See Also
--------
numpy.append : Equivalent function in the top-level NumPy module.

Examples
--------
>>> import numpy as np
>>> import numpy.ma as ma
>>> a = ma.masked_values([1, 2, 3], 2)
>>> b = ma.masked_values([[4, 5, 6], [7, 8, 9]], 7)
>>> ma.append(a, b)
masked_array(data=[1, --, 3, 4, 5, 6, --, 8, 9],
             mask=[False,  True, False, False, False, False,  True, False,
                   False],
       fill_value=999999)
- `allequal` (ID: 382b061d-e35c-4fcf-8b04-d566d52caf5a): Return True if all entries of a and b are equal, using
fill_value as a truth value where either or both are masked.

Parameters
----------
a, b : array_like
    Input arrays to compare.
fill_value : bool, optional
    Whether masked values in a or b are considered equal (True) or not
    (False).

Returns
-------
y : bool
    Returns True if the two arrays are equal within the given
    tolerance, False otherwise. If either array contains NaN,
    then False is returned.

See Also
--------
all, any
numpy.ma.allclose

Examples
--------
>>> import numpy as np
>>> a = np.ma.array([1e10, 1e-7, 42.0], mask=[0, 0, 1])
>>> a
masked_array(data=[10000000000.0, 1e-07, --],
             mask=[False, False,  True],
       fill_value=1e+20)

>>> b = np.array([1e10, 1e-7, -42.0])
>>> b
array([  1.00000000e+10,   1.00000000e-07,  -4.20000000e+01])
>>> np.ma.allequal(a, b, fill_value=False)
False
>>> np.ma.allequal(a, b)
True
- `allclose` (ID: 4b83da81-5a05-4625-93ae-327a46b0748b): Returns True if two arrays are element-wise equal within a tolerance.

This function is equivalent to `allclose` except that masked values
are treated as equal (default) or unequal, depending on the `masked_equal`
argument.

Parameters
----------
a, b : array_like
    Input arrays to compare.
masked_equal : bool, optional
    Whether masked values in `a` and `b` are considered equal (True) or not
    (False). They are considered equal by default.
rtol : float, optional
    Relative tolerance. The relative difference is equal to ``rtol * b``.
    Default is 1e-5.
atol : float, optional
    Absolute tolerance. The absolute difference is equal to `atol`.
    Default is 1e-8.

Returns
-------
y : bool
    Returns True if the two arrays are equal within the given
    tolerance, False otherwise. If either array contains NaN, then
    False is returned.

See Also
--------
all, any
numpy.allclose : the non-masked `allclose`.

Notes
-----
If the following equation is element-wise True, then `allclose` returns
True::

  absolute(`a` - `b`) <= (`atol` + `rtol` * absolute(`b`))

Return True if all elements of `a` and `b` are equal subject to
given tolerances.

Examples
--------
>>> import numpy as np
>>> a = np.ma.array([1e10, 1e-7, 42.0], mask=[0, 0, 1])
>>> a
masked_array(data=[10000000000.0, 1e-07, --],
             mask=[False, False,  True],
       fill_value=1e+20)
>>> b = np.ma.array([1e10, 1e-8, -42.0], mask=[0, 0, 1])
>>> np.ma.allclose(a, b)
False

>>> a = np.ma.array([1e10, 1e-8, 42.0], mask=[0, 0, 1])
>>> b = np.ma.array([1.00001e10, 1e-9, -42.0], mask=[0, 0, 1])
>>> np.ma.allclose(a, b)
True
>>> np.ma.allclose(a, b, masked_equal=False)
False

Masked values are not compared directly.

>>> a = np.ma.array([1e10, 1e-8, 42.0], mask=[0, 0, 1])
>>> b = np.ma.array([1.00001e10, 1e-9, 42.0], mask=[0, 0, 1])
>>> np.ma.allclose(a, b)
True
>>> np.ma.allclose(a, b, masked_equal=False)
False
- `test_xerbla_override` (ID: 03f6df5b-fcba-424b-8f35-d8cec92f9bab): No description
- `test_vector_norm_empty` (ID: c7d95819-37c7-4395-9f92-855cea9406bb): No description
- `test_vector_norm` (ID: a9f6a963-c871-4b29-8e62-1bfd3da81575): No description
- `test_unsupported_commontype` (ID: 84eec2c7-b15b-47c6-ba5a-839d3a086ff9): No description
- `test_trace` (ID: dcf36692-81f6-43cc-b8b4-ba9592549815): No description
- `test_tensordot` (ID: f641cb3f-f132-412d-a946-2406c16de8f1): No description
- `test_sdot_bug_8577` (ID: 4edcf12b-dcd0-42fc-b4e2-8ecc3d1af1bd): No description
- `test_reduced_rank` (ID: 54bf10f1-eb0a-4cea-b1ce-4e4952e595f9): No description
- `test_pinv_rtol_arg` (ID: 4a7fd85f-e7ba-4fab-8e33-f07aaab73fcd): No description
- `test_matrix_transpose` (ID: 00f69c45-8aca-4f72-8ba7-6f406a55e9ea): No description
- `test_matrix_norm_empty` (ID: a7282c13-f149-4221-b316-57fa96f37a04): No description
- `test_matrix_norm` (ID: 3b05fd7b-894b-41d5-b797-a814257bdd17): No description
- `test_matmul` (ID: 0f934991-b0c3-41d7-b3d6-beb5e712a989): No description
- `test_generalized_raise_multiloop` (ID: 6afbaff1-96f4-4037-a712-3951a978de25): No description
- `test_diagonal` (ID: 617c1ea6-5bc1-488a-8e06-d357e22e87e4): No description
- `test_cross` (ID: 63bca829-924a-44bf-aee5-90e2b9d84dbc): No description
- `test_byteorder_check` (ID: 455b8f21-616f-4afe-974a-d9a5e0aa6c09): No description
- `test_blas64_geqrf_lwork_smoketest` (ID: 23cb20fe-30bd-4a0f-a7d7-245870430ee9): No description
- `test_blas64_dot` (ID: e5d90283-a1d0-4f1d-b9cf-65ba84881e93): No description
- `identity_like_generalized` (ID: f705b93f-7649-4990-b706-8b57f03f1efb): No description
- `get_rtol` (ID: ca628821-b14a-4acc-9d6b-a45cd6b33d82): No description
- `get_real_dtype` (ID: 1f816137-7838-410c-8b48-9e90f3f48127): No description
- `get_complex_dtype` (ID: 1915755f-0e42-4dcc-ab0c-0bfb6485c6af): No description
- `consistent_subclass` (ID: a293c9f1-cfa6-4ea1-aaf2-5a9c7e51c011): No description
- `apply_tag` (ID: 54ebb4ce-0dac-41ce-b898-301bbd866cd4): Add the given tag (a string) to each of the cases (a list of LinalgCase
objects)
- `test_qr_mode_full_future_warning` (ID: 33e0ac5a-7ae1-492c-9710-8a767641304d): Check mode='full' FutureWarning.

In numpy 1.8 the mode options 'full' and 'economic' in linalg.qr were
deprecated. The release date will probably be sometime in the summer
of 2013.
- `zungqr` (ID: 61895bce-adc7-45c7-8e0f-aa8c3d58036f): No description
- `zgeqrf` (ID: ff1d1a0b-eb9a-48e5-b018-be56c93820dd): No description
- `zgelsd` (ID: 72dca895-d60a-4625-a862-13f6abe833a4): No description
- `xerbla` (ID: b6b71890-179f-4141-9590-66a62d782fe3): No description
- `scrubF2CSource` (ID: a59440ce-5324-44b4-9d86-e7687ef6c101): No description
- `runF2C` (ID: 1519a719-487b-4c32-b974-b2e176c58482): No description
- `printRoutineNames` (ID: bf9a012b-3944-4168-b951-2308f98a95e8): No description
- `main` (ID: e37ed7a2-4831-4fc6-a986-2ef983865daf): No description
- `getWrappedRoutineNames` (ID: 6a45298c-2e60-4deb-92d9-00a37bc4fd14): No description
- `getLapackRoutines` (ID: ebcc541a-4ff0-47b1-8413-217e3c775a3a): No description
- `ensure_executable` (ID: 8d7e5823-e99a-4ec5-a0fc-ecdc76eeef19): No description
- `dumpRoutineNames` (ID: ba8d466c-2c89-4124-980f-9afa2e0b61d1): No description
- `create_name_header` (ID: 9786d9e9-dbe4-48aa-91ec-85f4e93455c9): No description
- `concatenateRoutines` (ID: 6e8e25f8-064e-411b-a470-52872ef427b7): No description
- `lineType` (ID: 3241715c-cf65-4d07-a86a-cd35be8cdd7b): Return the type of a line of Fortran code.
- `isLabel` (ID: 542ee237-a896-4685-af1f-d9e82ce31418): No description
- `isContinuation` (ID: ebc43c64-59a6-4bfa-989d-5f2cdf528394): No description
- `isComment` (ID: 25be1eeb-4ff1-4a5e-8d1c-26da612ad009): No description
- `isBlank` (ID: 482ac2a7-6ec3-453d-acec-7084050e41cb): No description
- `getDependencies` (ID: 1e45546e-eb89-404a-a917-68f837fa94f2): For a Fortran source file, return a list of routines declared as EXTERNAL
in it.
- `fortranSourceLines` (ID: aa0292ad-16e9-409c-b110-00250d2d94ff): Return an iterator over statement lines of a Fortran source file.

Comment and blank lines are stripped out, and continuation lines are
merged.
- `dorgqr` (ID: 69dc4c8b-bb6f-4af9-a3d5-429bb00391fd): No description
- `dgeqrf` (ID: 399ba140-0914-47b9-a02f-b554b8cde184): No description
- `dgelsd` (ID: 8256f723-d266-4dd5-b134-eb09981bf6ff): No description
- `sep_seq` (ID: e714a747-f4cf-42cf-acc7-7123f17f022f): No description
- `scrubSource` (ID: 434ae0f0-9f35-4732-9824-7ddc38dda5af): No description
- `scrubFtnlen` (ID: 2297329a-4467-43b9-b0b7-497c6d195557): No description
- `runScanner` (ID: d1b6b7a6-ce79-4a26-86e1-2e20ab9763a2): No description
- `replaceDlamch` (ID: 461f707b-487c-4a93-8205-b5380566722c): Replace dlamch_ calls with appropriate macros
- `removeSubroutinePrototypes` (ID: 16b12e40-5ff7-49f4-ac8c-260d061dc3ad): No description
- `removeHeader` (ID: 02df7e30-f99a-4766-ab6e-c88524146ec8): No description
- `removeBuiltinFunctions` (ID: e0505b20-6e89-4bd0-96b5-2db75b59d55d): No description
- `cleanSource` (ID: bdd1b82a-c356-4888-8a73-d4d377f3f4d6): No description
- `cleanComments` (ID: 7102ce74-21cc-4930-bc9b-447dd3f38f99): No description
- `test_info_method_heading` (ID: 83150748-b7f2-43e6-87ce-4aed3e8bc4be): No description
- `test_drop_metadata_identity_and_copy` (ID: ddf4e974-77d5-451d-9ed7-70e81ab0f8a8): No description
- `test_drop_metadata` (ID: cbd029a9-5bbc-4946-ab99-ab941a05ff6b): No description
- `test_assert_raises_regex_context_manager` (ID: c0955d1f-73d7-4275-8a99-3c6afa146005): No description
- `assert_all` (ID: 6186754d-8736-49f8-8447-91a1a19df124): No description
- `test_tril_triu_with_inf` (ID: 8dbbb596-8d1e-442d-b79e-8bb88390d097): No description
- `test_tril_triu_ndim3` (ID: e4bd3aa1-02b7-44b2-b8c0-d13227991b31): No description
- `test_tril_triu_ndim2` (ID: 56ecc7c5-cafa-4e34-babb-065a47e9afba): No description
- `test_tril_triu_dtype` (ID: cac54992-e532-4a0b-9010-d3077e0db655): No description
- `test_tril_indices` (ID: 5163e16c-2de8-4376-97b5-3f52ff69c609): No description
- `test_mask_indices` (ID: 04397a72-1e28-4fcb-992a-c92cef5a84cd): No description
- `get_mat` (ID: 576f6b46-991c-4b90-93ac-28943c20f3dd): No description
- `test_writeable_memoryview` (ID: 29445bcb-b452-4c3a-96a3-bf2c6b24e430): No description
- `test_writeable` (ID: 74b49238-925a-4882-a2fe-c48c2373214e): No description
- `test_two_compatible_by_prepending_ones_input_shapes` (ID: f13f7ba8-4eaa-4402-87e4-7af021f95f6f): No description
- `test_two_compatible_by_ones_input_shapes` (ID: 9f661846-735e-4a5c-b792-ccdc84aa6188): No description
- `test_subclasses` (ID: f3e6418b-cde6-4494-ac9f-8f9096dc576f): No description
- `test_same_input_shapes` (ID: ebf61868-b355-4e2d-b05a-30993d9e8160): No description
- `test_same_as_ufunc` (ID: 0f874d96-3bee-4903-b1fd-9d825f5bb6f5): No description
- `test_same` (ID: 1ac267df-6ab6-47dc-9701-aae025ff21e5): No description
- `test_reference_types` (ID: 92785766-9207-4c22-ae46-9fe363dbc084): No description
- `test_one_off` (ID: 1842526e-9e99-4b32-baae-ae337766bb57): No description
- `test_incompatible_shapes_raise_valueerror` (ID: 4acca45f-e5a5-4f00-9ad6-cbdd550789fd): No description
- `test_broadcast_to_succeeds` (ID: ee316dd5-2aa9-4972-861c-b9be8f94f887): No description
- `test_broadcast_to_raises` (ID: 50c626f0-28a2-4c10-931a-5239ba98d450): No description
- `test_broadcast_shapes_succeeds` (ID: 398debc9-ab76-4529-8f35-fbba1cfc3221): No description
- `test_broadcast_shapes_raises` (ID: 05c3a0b8-91d3-4b0e-857f-3a8e5d94aa37): No description
- `test_broadcast_shape` (ID: 73c01056-59ff-44d4-94f8-e3f13f8d8cb0): No description
- `test_broadcast_kwargs` (ID: c915c659-1919-4ae0-95bb-eaec711deb9b): No description
- `test_as_strided` (ID: c1d0ba37-5932-4e4e-8942-5945ee458867): No description
- `assert_shapes_correct` (ID: 37ffff95-d4bb-4aca-9e18-fa176e72ac60): No description
- `assert_same_as_ufunc` (ID: afd1c3f6-ab79-4fd5-b36d-dbf1e0b21c65): No description
- `assert_incompatible_shapes_raise` (ID: b4339701-2405-4813-b7a8-040c3f3f634c): No description
- `as_strided_writeable` (ID: 2f5b58ee-02d6-40fd-bfa2-a22f092ba7da): No description
- `compare_results` (ID: 99616f9d-734b-4893-b077-c922f7678b5c): Compare lists of arrays.
- `test_unpackbits_large` (ID: e6d823bc-aa26-4c16-8260-7763283d1a01): No description
- `test_unpackbits_empty_with_axis` (ID: 273d03a0-cc24-4608-93d7-9ccc8a07395f): No description
- `test_unpackbits_empty` (ID: c6c07812-7134-4edb-9780-8e6f5070bd1f): No description
- `test_unpackbits` (ID: b50cf88f-7cfc-4267-8dcc-845f6f6baa38): No description
- `test_packbits_very_large` (ID: 8f120923-d34b-497c-a1bf-2b2e2f024dda): No description
- `test_packbits_large` (ID: 7501fb38-0690-47bc-ac30-d49b5b990907): No description
- `test_packbits_empty_with_axis` (ID: 4409b153-a1fb-4a47-8eed-2c61fba2b1c4): No description
- `test_packbits_empty` (ID: b4854587-0587-49ac-b4fe-e0db306fd15b): No description
- `test_packbits` (ID: eb315000-7b48-49c6-ba44-903334e70c29): No description
- `test_pack_unpack_order` (ID: 4ca7db8c-d221-4f23-9287-5777069becfe): No description
- `test_memmap_takes_fast_route` (ID: aa729cd0-83bc-4ce1-a5e2-719631eb8586): No description
- `test__replace_nan` (ID: 984b267e-082a-4584-a6a8-dc4349cb3553): Test that _replace_nan returns the original array if there are no
NaNs, not a copy.
- `test__nan_mask` (ID: b1ec96e4-30b7-4d8e-9c57-854efa4979be): No description
- `wrap_array_like` (ID: c69d604e-ae8e-4b5d-86b7-e2fee85b3aa8): No description
- `test_warn_on_skipped_data` (ID: b32fc866-26fb-43d9-9c68-bdcfecf3d801): No description
- `test_warn_on_no_data` (ID: 64b02a56-b7c4-43a4-a756-bab6a1d98617): Check that a UserWarning is emitted when no data is read from input.
- `test_unpack_structured` (ID: 04a367be-dde7-4405-aabb-3760d4f0e51e): No description
- `test_universal_newlines_quoted` (ID: 73fa75a6-cc42-4168-9d9a-e1c68907caa5): No description
- `test_unicode_with_converter` (ID: 27cbbf40-02a1-4137-b58e-66aa8cb2e44b): No description
- `test_unicode_whitespace_stripping_complex` (ID: 87badaf5-2d41-497a-980b-c172a7f43ba6): No description
- `test_unicode_whitespace_stripping` (ID: ca8703dc-b5fe-47e3-83d5-a9268499090e): No description
- `test_structured_dtype_with_shape` (ID: b7eb11a5-64b7-4898-b680-166bf665c92c): No description
- `test_structured_dtype_with_quotes` (ID: 23fdd5f4-32e8-4dce-8501-ab12bc5b8392): No description
- `test_structured_dtype_with_multi_shape` (ID: 2036d9d1-5b7f-4eff-9b67-7af911d73d1f): No description
- `test_structured_dtype_offsets` (ID: afcf15c2-951b-42a6-8d62-a492aacd7a64): No description
- `test_structured_dtype_and_skiprows_no_empty_lines` (ID: 827a0180-c928-43b3-94c1-0c3e2f822c19): No description
- `test_string_no_length_given` (ID: affb151a-b430-4ee7-9cab-2a21956d8c2c): The given dtype is just 'S' or 'U' with no length. In these cases, the
length of the resulting dtype is determined by the longest string found
in the file.
- `test_str_dtype_unit_discovery_with_converter` (ID: e7047ed2-2a06-4bc2-b761-4d09ea7fd593): No description
- `test_skiprow_exceeding_maxrows_exceeding_chunksize` (ID: 2d0053d2-c60a-4a21-abaa-0c2f7599b9e5): No description
- `test_scientific_notation` (ID: 27482d78-346e-4574-8494-cebd26377b15): Test that both 'e' and 'E' are parsed correctly.
- `test_read_huge_row` (ID: 36be2b7f-511f-4545-843e-493ea70d5fda): No description
- `test_read_from_generator_multitype` (ID: a3e63892-29ee-4b15-9f10-867af88e6774): No description
- `test_read_from_generator` (ID: 368ce884-a424-4824-895d-78aceafc2a44): No description
- `test_read_from_bad_generator` (ID: 3509fa82-2195-4fa3-addb-d00feef51e80): No description
- `test_ragged_usecols` (ID: c44453e6-9c01-4539-9f8a-8d15a97e1498): No description
- `test_ragged_error` (ID: 3ee8e7ef-01b7-4ae8-95d4-cc29533b21b4): No description
- `test_quoted_field_with_whitepace_delimiter` (ID: 0d3c8bf8-a9e3-4759-b8e3-a71fa0faa856): No description
- `test_quoted_field_is_not_empty_nonstrict` (ID: 948e8354-37ea-49ca-8665-08d3d610edde): No description
- `test_quoted_field_is_not_empty` (ID: b634bdb3-6d5d-41f9-af4c-7d140264a1f7): No description
- `test_quoted_field` (ID: 27f1c005-a116-4cb5-9271-a72cdcb391d4): No description
- `test_quotechar_multichar_error` (ID: fe736616-6bbe-40d2-a078-f92ffb5b756f): No description
- `test_quote_support_default` (ID: 8a30d3da-cb72-4896-88f2-9346be87d0b8): Support for quoted fields is disabled by default.
- `test_parametric_unit_discovery` (ID: 802eb980-4624-42da-88c2-800eed0bcf23): Check that the correct unit (e.g. month, day, second) is discovered from
the data when a user specifies a unitless datetime.
- `test_object_cleanup_on_read_error` (ID: 91b35d4c-fcbf-47f2-8018-f522cbde4fd5): No description
- `test_null_character` (ID: feda074e-af28-45d7-a5b1-63370d3a2890): No description
- `test_nul_character_error` (ID: a1778453-e18f-4771-9349-aa9185dde76e): No description
- `test_no_thousands_support` (ID: 13f04871-178d-4065-a697-56c66a9a0c65): No description
- `test_nested_structured_subarray` (ID: 01f757ed-5fdb-46f4-82fb-5c21733892c6): No description
- `test_ndmin_single_row_or_col` (ID: 7453f4cc-e596-41e7-860d-d70e57024dbb): No description
- `test_maxrows_no_blank_lines` (ID: 302a3cc6-f975-4ed5-80b7-d022d59ceb93): No description
- `test_maxrows_exceeding_chunksize` (ID: 50e70bf8-0644-4d38-9623-f551c5660dc4): No description
- `test_large_unicode_characters` (ID: e5dc0bd3-36cc-4947-8339-aefe3b7fe453): No description
- `test_iterator_fails_getting_next_line` (ID: 170d04da-3d05-422c-ab9d-dea63a4f2cdf): No description
- `test_invalid_converter` (ID: c5f17e6b-a982-4e25-a6d5-c4b6fe0de5e6): No description
- `test_integer_signs` (ID: 569de5ce-4851-4d38-a93a-51f5563e716c): No description
- `test_implicit_cast_float_to_int_fails` (ID: e950ada4-2fd2-414b-8e14-7d40fdeb56aa): No description
- `test_huge_float` (ID: 61147487-6148-4a5c-8ccc-d0ebf3338b89): No description
- `test_good_newline_in_iterator` (ID: 799f94bf-ec01-4027-8e24-6bcc83ef46dc): No description
- `test_float_conversion` (ID: 705f5212-f91e-4a54-99a6-9291eae4e3ad): Some tests that the conversion to float64 works as accurately as the
Python built-in `float` function. In a naive version of the float parser,
these strings resulted in values that were off by an ULP or two.
- `test_field_growing_cases` (ID: 7d36f8ee-9402-4b96-9906-5b96aa37653e): No description
- `test_exception_noninteger_row_limits` (ID: f1bf7245-053c-4717-b24b-c753c2e8e22a): No description
- `test_exception_negative_row_limits` (ID: a59d617f-1121-410e-a778-a790faa768d3): skiprows and max_rows should raise for negative parameters.
- `test_exception_message_bad_values` (ID: 602f3da1-55bd-465e-b146-23e0c7bcaeab): No description
- `test_empty_usecols` (ID: de120fee-c44b-4755-8ece-a58d608df969): No description
- `test_delimiter_quotechar_collision_raises` (ID: 8ae9f82f-480d-4fad-b333-d45a4dfcb8bf): No description
- `test_delimiter_comment_collision_raises` (ID: ce31ad11-416d-4995-88b8-71efa8fd25cd): No description
- `test_delimiter_and_multiple_comments_collision_raises` (ID: 089b338e-1657-4e75-8c86-18939e5e10cc): No description
- `test_converters_negative_indices_with_usecols` (ID: b4d97b11-c12a-4066-8e61-5e47135001f9): No description
- `test_converters_negative_indices` (ID: 12ec5ffa-228b-47f5-afbd-b014e31be8ab): No description
- `test_converters_dict_raises_val_not_callable` (ID: 27c38d68-33d1-41b7-9c99-e0f4dc32b923): No description
- `test_converters_dict_raises_non_integer_key` (ID: 1a818a6f-af64-42da-979d-921cabaf7943): No description
- `test_converters_dict_raises_non_col_key` (ID: 62656a51-c28e-487b-9c14-4983230a8d39): No description
- `test_converter_with_unicode_dtype` (ID: 8a9e6141-93d1-40a0-8333-4b5a19fba185): With the 'bytes' encoding, tokens are encoded prior to being
passed to the converter. This means that the output of the converter may
be bytes instead of unicode as expected by `read_rows`.

This test checks that outputs from the above scenario are properly decoded
prior to parsing by `read_rows`.
- `test_converter_with_structured_dtype` (ID: 7f831bce-0a52-4f75-93e2-dc4e1e85e8eb): No description
- `test_control_characters_as_bytes` (ID: edeeedda-7ad4-4e46-936f-e5cdc8f170c2): Byte control characters (comments, delimiter) are supported.
- `test_control_character_newline_raises` (ID: 13d080b4-9ff0-4c63-a76e-42346d77c166): No description
- `test_control_character_empty` (ID: 7c3104ff-a467-4307-b37b-82445effad07): No description
- `test_consecutive_quotechar_escaped` (ID: 75ea85a3-643a-4d3f-955b-b216a4092c58): No description
- `test_complex_parsing` (ID: f404193b-ede5-4358-b56a-ddf8615f63be): No description
- `test_comment_quotechar_collision_raises` (ID: f17af1e1-d957-4603-b76a-875f9afdcd54): No description
- `test_comment_multiple_chars` (ID: ebde4dd3-f44c-4775-b550-8290ff08fd91): No description
- `test_comment_multichar_error_with_quote` (ID: 0045a746-5c8a-41e7-afe3-d92bd1ec56be): No description
- `test_collision_with_default_delimiter_raises` (ID: 01c0d04b-e5e2-461f-bfe9-7ec6ec00ccf5): No description
- `test_character_not_bytes_compatible` (ID: 67966a81-e6cf-4a00-bd0d-153a7adc2fd9): Test exception when a character cannot be encoded as 'S'.
- `test_byteswapping_and_unaligned` (ID: 01a99a0f-e336-4dfe-9cf2-7273c3583b87): No description
- `test_bool` (ID: c3f9d3b6-736d-40ab-82ce-b4aafee0454b): No description
- `test_blank_lines_spaces_delimit` (ID: dcfc88c3-5f8b-421f-8203-8ea16768533c): No description
- `test_blank_lines_normal_delimiter` (ID: dacc6ffd-0ffb-4859-af89-3d60a7f3cbc0): No description
- `test_bad_newline_in_iterator` (ID: d4bb7c19-5230-4db1-8395-ee371d09be5c): No description
- `test_bad_ndmin` (ID: 7e2c132d-87e6-47a4-88a8-65f5144c2385): No description
- `test_bad_complex` (ID: 907facc8-81a5-44b5-82d5-f76a722434ec): No description
- `mixed_types_structured` (ID: d717d474-df64-45a9-82b9-845c12b427fc): Fixture providing heterogeneous input data with a structured dtype, along
with the associated structured array.
- `test_savez_nopickle` (ID: a02e7aa7-6535-4e82-82aa-36cfbfc28487): No description
- `test_npzfile_dict` (ID: ea77dbfa-6f05-4b60-ba62-b9725399e722): No description
- `test_load_refcount` (ID: 05419e4d-da58-4959-b545-0052e26c7459): No description
- `test_load_multiple_arrays_until_eof` (ID: 970b1f1f-bc15-408e-a0af-6c9281921444): No description
- `test_gzip_loadtxt_from_string` (ID: 7805ec1f-667f-4237-9a94-a447313f5474): No description
- `test_gzip_loadtxt` (ID: 4cacb3e8-34fa-48ef-80f7-8a360fa22b92): No description
- `test_gzip_load` (ID: 685a30ad-a2a7-4384-bc08-1f9d019d744b): No description
- `test_ducktyping` (ID: 009ef93d-b200-4af0-a4ff-d84843129463): No description
- `strptime` (ID: 7b6028b1-b912-44cc-955f-d78cc2e1ae9e): This function is available in the datetime module only from Python >=
2.5.
- `test_ndindex` (ID: 27a4d3eb-9234-4ec0-89b3-c1d6ecf2d717): No description
- `test_diag_indices` (ID: ee7dd0c1-4b79-4196-8d36-e46f3eb00e5c): No description
- `test_c_` (ID: 504c358f-80d1-42b1-8e0a-790b7633b689): No description
- `test_cumulative_include_initial` (ID: f46e8acd-1631-45a5-b728-4bac7b5e44ad): No description
- `test_any_and_all_result_dtype` (ID: 9f095767-5551-4714-b840-8d515d9fd915): No description
- `get_mat` (ID: 386c4e33-72b9-43d2-b775-fd405416a76d): No description
- `test_write_version` (ID: db21d88c-5fbf-4e9a-8929-0b0420a33da2): No description
- `test_version_2_0_memmap` (ID: 00bce4f4-84aa-4c9e-9f9e-273429749ade): No description
- `test_version_2_0` (ID: cfe1074f-0a97-4c96-a70b-cdd0467b6c36): No description
- `test_unicode_field_names` (ID: 874be8f7-11a1-474f-939a-3714bd928a77): No description
- `test_roundtrip_truncated` (ID: db96e8d6-d552-4572-9d3b-9eff56491ecb): No description
- `test_roundtrip_randsize` (ID: 3a7cfc2a-6861-41bf-8990-6d8496f20763): No description
- `test_roundtrip` (ID: 61e6b666-18f1-4b15-8847-16fcc1971e68): No description
- `test_read_version_1_0_bad_magic` (ID: 3268db05-4f02-4c3d-9f86-bc7f0bd923f1): No description
- `test_read_magic_bad_magic` (ID: 95254678-4bd5-4858-a800-ae38957e1c9a): No description
- `test_read_magic` (ID: 425392c4-eca9-410c-8441-af880b9897a7): No description
- `test_read_array_header_2_0` (ID: 5dd2f697-7a99-4ba6-9755-231aaabaf56b): No description
- `test_read_array_header_1_0` (ID: 5ad06cd9-4981-4cdf-859c-22b07cfe6f47): No description
- `test_python2_python3_interoperability` (ID: 795a78cd-5304-435a-9bf0-ca20f20936e3): No description
- `test_pickle_python2_python3` (ID: 6a709de2-4da2-4312-b855-2f4c593155d5): No description
- `test_pickle_disallow` (ID: 70e39053-fe5c-4075-9e55-95c2cd95f49f): No description
- `test_metadata_dtype` (ID: 4f9ab497-c2f3-486c-b370-1aa01c70bd94): No description
- `test_memmap_roundtrip` (ID: 02bbcb70-a9ec-4e06-a8a5-90793df158e4): No description
- `test_long_str` (ID: 2530d18c-7a7f-4446-8361-fed041afeb89): No description
- `test_load_padded_dtype` (ID: c63ecc1a-9759-436a-810f-b1d181f4cd6a): No description
- `test_large_header` (ID: c8273f18-0ba3-44ab-bad7-a4c2aca1fe22): No description
- `test_large_file_support` (ID: a026ee44-64a5-4e76-a69e-0a0557e5fcec): No description
- `test_large_archive` (ID: 497b03ac-2833-4371-ba6d-bfbe3ac5f210): No description
- `test_huge_header_npz` (ID: 9fbf5787-4a4b-47a1-99f7-a7b1618bd147): No description
- `test_huge_header` (ID: 42fa81b8-3427-42dd-9b69-9a46d1e21726): No description
- `test_header_growth_axis` (ID: b4af565d-308c-4d18-8198-ef99ca675891): No description
- `test_file_truncated` (ID: f982962a-add3-4a1a-ad03-c742a0aa20dd): No description
- `test_empty_npz` (ID: 475540e2-3f43-47dc-9ce4-285ae48864f5): No description
- `test_descr_to_dtype` (ID: b3818767-52b2-47f7-a375-8e3fe2f2a2f1): No description
- `test_compressed_roundtrip` (ID: d607cc35-304d-4e12-966d-419c2f7cf68b): No description
- `test_bad_magic_args` (ID: 0e790840-ffae-4673-818c-f9813998bb4d): No description
- `test_bad_header` (ID: 2822bc50-1a5c-4891-b15b-7cda1c87f88c): No description
- `roundtrip_truncated` (ID: 2539549b-aca7-4037-945c-fd3ea681fbc6): No description
- `roundtrip_randsize` (ID: a8633516-b5ce-43cb-a76d-4aeb0514a431): No description
- `roundtrip` (ID: 49252be3-ca22-436d-a3c7-e960a2786fed): No description
- `assert_equal_` (ID: c45f0a74-2dcf-472c-8d86-70abff8cdc8d): No description
- `test` (ID: d55c78a7-389e-4354-8827-40826d682937): No description
- `test_unsupported_mode` (ID: 2f1dca86-0bc1-4f89-a951-7b2196799f88): No description
- `test_unicode_mode` (ID: 99f95316-3409-413d-bdcd-c7d6c1892ab2): No description
- `test_object_input` (ID: 7cd5f753-39de-4321-b420-73fbf8b22c28): No description
- `test_non_contiguous_array` (ID: 9247bddd-1058-4755-82ce-277779bc270d): No description
- `test_memory_layout_persistence` (ID: 688760ed-4b8e-4cf1-885a-de19aa790cd9): Test if C and F order is preserved for all pad modes.
- `test_legacy_vector_functionality` (ID: 5595b61f-31f0-445a-9a57-f3af5798f995): No description
- `test_kwargs` (ID: 3edc5a1a-3500-46bc-8693-e7a20b3095ca): Test behavior of pad's kwargs for the given mode.
- `test_dtype_persistence` (ID: 6745220b-d2df-4cde-a0a2-46d72893bfab): No description
- `test_constant_zero_default` (ID: 7b4ab365-98a8-4d04-b422-9a74e84d3d05): No description
- `test_version_1_point_10` (ID: a848ec97-ba87-4129-a11b-a0b3cec93d54): No description
- `test_raises` (ID: 1ad36709-04fb-45b5-8016-236ded5548d8): No description
- `test_main_versions` (ID: ce73a451-f549-4fc1-8d94-a4968b877a53): No description
- `test_dev_version` (ID: 08a1dcc4-9799-43fb-a6bf-6d5921dd5c01): No description
- `test_dev_a_b_rc_mixed` (ID: 7881362e-561c-4bbd-803a-153f121bdcda): No description
- `test_dev0_version` (ID: f0b1d693-7280-4390-ac5a-cab0a2b536ee): No description
- `test_dev0_a_b_rc_mixed` (ID: 662aac4d-6997-453d-8d4c-ee2c33391e6c): No description
- `test_alpha_beta_rc` (ID: 933af8db-2422-4525-a6f9-2af1bb9b3428): No description
- `valid_textfile` (ID: ee5fa469-adde-4756-99ed-58604eb0ed86): No description
- `valid_httpurl` (ID: ecb976bf-dc26-4fbd-8615-4082a9672888): No description
- `valid_httpfile` (ID: 25a3a06d-2545-4be1-be3c-5065f3766cc8): No description
- `valid_baseurl` (ID: 365c33f8-7dd4-4f7b-bc90-2e30e126d020): No description
- `urlopen_stub` (ID: 5d510229-f1df-42b2-88a2-487b373efa2b): Stub to replace urlopen for testing.
- `test_del_attr_handling` (ID: 5ce7a14c-9750-4fc1-bc1d-584e136f3d54): No description
- `teardown_module` (ID: 98990baf-05e6-45fd-8ef7-64e1b88c263a): No description
- `setup_module` (ID: b13f2032-8ff6-4088-acaa-c259fa7d8ff1): No description
- `invalid_textfile` (ID: c037f573-8bea-4667-8590-c14c0b32696f): No description
- `invalid_httpurl` (ID: 6a326ac0-b467-41bd-a388-175f984a4244): No description
- `invalid_httpfile` (ID: 4e5bfcf0-18a0-4621-b230-e55e65310f1a): No description
- `invalid_baseurl` (ID: 8611f65f-d49f-46fc-9406-83ec05338651): No description
- `unstructured_to_structured` (ID: 60905c8f-b637-4a7b-94bd-33a9bf2c889e): Converts an n-D unstructured array into an (n-1)-D structured array.

The last dimension of the input array is converted into a structure, with
number of field-elements equal to the size of the last dimension of the
input array. By default all output fields have the input array's dtype, but
an output structured dtype with an equal number of fields-elements can be
supplied instead.

Nested fields, as well as each element of any subarray fields, all count
towards the number of field-elements.

Parameters
----------
arr : ndarray
   Unstructured array or dtype to convert.
dtype : dtype, optional
   The structured dtype of the output array
names : list of strings, optional
   If dtype is not supplied, this specifies the field names for the output
   dtype, in order. The field dtypes will be the same as the input array.
align : boolean, optional
   Whether to create an aligned memory layout.
copy : bool, optional
    See copy argument to `numpy.ndarray.astype`. If true, always return a
    copy. If false, and `dtype` requirements are satisfied, a view is
    returned.
casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
    See casting argument of `numpy.ndarray.astype`. Controls what kind of
    data casting may occur.

Returns
-------
structured : ndarray
   Structured array with fewer dimensions.

Examples
--------
>>> import numpy as np

>>> from numpy.lib import recfunctions as rfn
>>> dt = np.dtype([('a', 'i4'), ('b', 'f4,u2'), ('c', 'f4', 2)])
>>> a = np.arange(20).reshape((4,5))
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
>>> rfn.unstructured_to_structured(a, dt)
array([( 0, ( 1.,  2), [ 3.,  4.]), ( 5, ( 6.,  7), [ 8.,  9.]),
       (10, (11., 12), [13., 14.]), (15, (16., 17), [18., 19.])],
      dtype=[('a', '<i4'), ('b', [('f0', '<f4'), ('f1', '<u2')]), ('c', '<f4', (2,))])
- `structured_to_unstructured` (ID: 8225f874-fe20-42d2-a33a-85d86fd472f2): Converts an n-D structured array into an (n+1)-D unstructured array.

The new array will have a new last dimension equal in size to the
number of field-elements of the input array. If not supplied, the output
datatype is determined from the numpy type promotion rules applied to all
the field datatypes.

Nested fields, as well as each element of any subarray fields, all count
as a single field-elements.

Parameters
----------
arr : ndarray
   Structured array or dtype to convert. Cannot contain object datatype.
dtype : dtype, optional
   The dtype of the output unstructured array.
copy : bool, optional
    If true, always return a copy. If false, a view is returned if
    possible, such as when the `dtype` and strides of the fields are
    suitable and the array subtype is one of `numpy.ndarray`,
    `numpy.recarray` or `numpy.memmap`.

    .. versionchanged:: 1.25.0
        A view can now be returned if the fields are separated by a
        uniform stride.

casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
    See casting argument of `numpy.ndarray.astype`. Controls what kind of
    data casting may occur.

Returns
-------
unstructured : ndarray
   Unstructured array with one more dimension.

Examples
--------
>>> import numpy as np

>>> from numpy.lib import recfunctions as rfn
>>> a = np.zeros(4, dtype=[('a', 'i4'), ('b', 'f4,u2'), ('c', 'f4', 2)])
>>> a
array([(0, (0., 0), [0., 0.]), (0, (0., 0), [0., 0.]),
       (0, (0., 0), [0., 0.]), (0, (0., 0), [0., 0.])],
      dtype=[('a', '<i4'), ('b', [('f0', '<f4'), ('f1', '<u2')]), ('c', '<f4', (2,))])
>>> rfn.structured_to_unstructured(a)
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

>>> b = np.array([(1, 2, 5), (4, 5, 7), (7, 8 ,11), (10, 11, 12)],
...              dtype=[('x', 'i4'), ('y', 'f4'), ('z', 'f8')])
>>> np.mean(rfn.structured_to_unstructured(b[['x', 'z']]), axis=-1)
array([ 3. ,  5.5,  9. , 11. ])
- `stack_arrays` (ID: 4f80543c-2747-496c-a1b7-66eab7b1de59): Superposes arrays fields by fields

Parameters
----------
arrays : array or sequence
    Sequence of input arrays.
defaults : dictionary, optional
    Dictionary mapping field names to the corresponding default values.
usemask : {True, False}, optional
    Whether to return a MaskedArray (or MaskedRecords is
    `asrecarray==True`) or a ndarray.
asrecarray : {False, True}, optional
    Whether to return a recarray (or MaskedRecords if `usemask==True`)
    or just a flexible-type ndarray.
autoconvert : {False, True}, optional
    Whether automatically cast the type of the field to the maximum.

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> x = np.array([1, 2,])
>>> rfn.stack_arrays(x) is x
True
>>> z = np.array([('A', 1), ('B', 2)], dtype=[('A', '|S3'), ('B', float)])
>>> zz = np.array([('a', 10., 100.), ('b', 20., 200.), ('c', 30., 300.)],
...   dtype=[('A', '|S3'), ('B', np.double), ('C', np.double)])
>>> test = rfn.stack_arrays((z,zz))
>>> test
masked_array(data=[(b'A', 1.0, --), (b'B', 2.0, --), (b'a', 10.0, 100.0),
                   (b'b', 20.0, 200.0), (b'c', 30.0, 300.0)],
             mask=[(False, False,  True), (False, False,  True),
                   (False, False, False), (False, False, False),
                   (False, False, False)],
       fill_value=(b'N/A', 1e+20, 1e+20),
            dtype=[('A', 'S3'), ('B', '<f8'), ('C', '<f8')])
- `require_fields` (ID: 42c0e965-ab12-4519-abb5-2598453685f9): Casts a structured array to a new dtype using assignment by field-name.

This function assigns from the old to the new array by name, so the
value of a field in the output array is the value of the field with the
same name in the source array. This has the effect of creating a new
ndarray containing only the fields "required" by the required_dtype.

If a field name in the required_dtype does not exist in the
input array, that field is created and set to 0 in the output array.

Parameters
----------
a : ndarray
   array to cast
required_dtype : dtype
   datatype for output array

Returns
-------
out : ndarray
    array with the new dtype, with field values copied from the fields in
    the input array with the same name

Examples
--------
>>> import numpy as np

>>> from numpy.lib import recfunctions as rfn
>>> a = np.ones(4, dtype=[('a', 'i4'), ('b', 'f8'), ('c', 'u1')])
>>> rfn.require_fields(a, [('b', 'f4'), ('c', 'u1')])
array([(1., 1), (1., 1), (1., 1), (1., 1)],
  dtype=[('b', '<f4'), ('c', 'u1')])
>>> rfn.require_fields(a, [('b', 'f4'), ('newf', 'u1')])
array([(1., 0), (1., 0), (1., 0), (1., 0)],
  dtype=[('b', '<f4'), ('newf', 'u1')])
- `repack_fields` (ID: ca9205cd-5024-4fcc-bfc1-a7cd7b8c278b): Re-pack the fields of a structured array or dtype in memory.

The memory layout of structured datatypes allows fields at arbitrary
byte offsets. This means the fields can be separated by padding bytes,
their offsets can be non-monotonically increasing, and they can overlap.

This method removes any overlaps and reorders the fields in memory so they
have increasing byte offsets, and adds or removes padding bytes depending
on the `align` option, which behaves like the `align` option to
`numpy.dtype`.

If `align=False`, this method produces a "packed" memory layout in which
each field starts at the byte the previous field ended, and any padding
bytes are removed.

If `align=True`, this methods produces an "aligned" memory layout in which
each field's offset is a multiple of its alignment, and the total itemsize
is a multiple of the largest alignment, by adding padding bytes as needed.

Parameters
----------
a : ndarray or dtype
   array or dtype for which to repack the fields.
align : boolean
   If true, use an "aligned" memory layout, otherwise use a "packed" layout.
recurse : boolean
   If True, also repack nested structures.

Returns
-------
repacked : ndarray or dtype
   Copy of `a` with fields repacked, or `a` itself if no repacking was
   needed.

Examples
--------
>>> import numpy as np

>>> from numpy.lib import recfunctions as rfn
>>> def print_offsets(d):
...     print("offsets:", [d.fields[name][1] for name in d.names])
...     print("itemsize:", d.itemsize)
...
>>> dt = np.dtype('u1, <i8, <f8', align=True)
>>> dt
dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['u1', '<i8', '<f8'], 'offsets': [0, 8, 16], 'itemsize': 24}, align=True)
>>> print_offsets(dt)
offsets: [0, 8, 16]
itemsize: 24
>>> packed_dt = rfn.repack_fields(dt)
>>> packed_dt
dtype([('f0', 'u1'), ('f1', '<i8'), ('f2', '<f8')])
>>> print_offsets(packed_dt)
offsets: [0, 1, 9]
itemsize: 17
- `rename_fields` (ID: eb333d60-b64e-46f1-9502-39116c5172d2): Rename the fields from a flexible-datatype ndarray or recarray.

Nested fields are supported.

Parameters
----------
base : ndarray
    Input array whose fields must be modified.
namemapper : dictionary
    Dictionary mapping old field names to their new version.

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> a = np.array([(1, (2, [3.0, 30.])), (4, (5, [6.0, 60.]))],
...   dtype=[('a', int),('b', [('ba', float), ('bb', (float, 2))])])
>>> rfn.rename_fields(a, {'a':'A', 'bb':'BB'})
array([(1, (2., [ 3., 30.])), (4, (5., [ 6., 60.]))],
      dtype=[('A', '<i8'), ('b', [('ba', '<f8'), ('BB', '<f8', (2,))])])
- `recursive_fill_fields` (ID: b2b19e5e-1b35-4426-bfb4-2270384999a2): Fills fields from output with fields from input,
with support for nested structures.

Parameters
----------
input : ndarray
    Input array.
output : ndarray
    Output array.

Notes
-----
* `output` should be at least the same size as `input`

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> a = np.array([(1, 10.), (2, 20.)], dtype=[('A', np.int64), ('B', np.float64)])
>>> b = np.zeros((3,), dtype=a.dtype)
>>> rfn.recursive_fill_fields(a, b)
array([(1, 10.), (2, 20.), (0,  0.)], dtype=[('A', '<i8'), ('B', '<f8')])
- `rec_join` (ID: e1d9b7be-ff1b-4cb8-94e6-67ec1658d5e2): Join arrays `r1` and `r2` on keys.
Alternative to join_by, that always returns a np.recarray.

See Also
--------
join_by : equivalent function
- `rec_drop_fields` (ID: 4e362c33-3fc2-49df-9869-ca17e8978735): Returns a new numpy.recarray with fields in `drop_names` dropped.
- `rec_append_fields` (ID: ac77b8f8-fa38-42ef-ba9c-90177a38df13): Add new fields to an existing array.

The names of the fields are given with the `names` arguments,
the corresponding values with the `data` arguments.
If a single field is appended, `names`, `data` and `dtypes` do not have
to be lists but just values.

Parameters
----------
base : array
    Input array to extend.
names : string, sequence
    String or sequence of strings corresponding to the names
    of the new fields.
data : array or sequence of arrays
    Array or sequence of arrays storing the fields to add to the base.
dtypes : sequence of datatypes, optional
    Datatype or sequence of datatypes.
    If None, the datatypes are estimated from the `data`.

See Also
--------
append_fields

Returns
-------
appended_array : np.recarray
- `merge_arrays` (ID: 0adc7120-0e9d-43c7-83f6-5f6b67a58bee): Merge arrays field by field.

Parameters
----------
seqarrays : sequence of ndarrays
    Sequence of arrays
fill_value : {float}, optional
    Filling value used to pad missing data on the shorter arrays.
flatten : {False, True}, optional
    Whether to collapse nested fields.
usemask : {False, True}, optional
    Whether to return a masked array or not.
asrecarray : {False, True}, optional
    Whether to return a recarray (MaskedRecords) or not.

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> rfn.merge_arrays((np.array([1, 2]), np.array([10., 20., 30.])))
array([( 1, 10.), ( 2, 20.), (-1, 30.)],
      dtype=[('f0', '<i8'), ('f1', '<f8')])

>>> rfn.merge_arrays((np.array([1, 2], dtype=np.int64),
...         np.array([10., 20., 30.])), usemask=False)
 array([(1, 10.0), (2, 20.0), (-1, 30.0)],
         dtype=[('f0', '<i8'), ('f1', '<f8')])
>>> rfn.merge_arrays((np.array([1, 2]).view([('a', np.int64)]),
...               np.array([10., 20., 30.])),
...              usemask=False, asrecarray=True)
rec.array([( 1, 10.), ( 2, 20.), (-1, 30.)],
          dtype=[('a', '<i8'), ('f1', '<f8')])

Notes
-----
* Without a mask, the missing value will be filled with something,
  depending on what its corresponding type:

  * ``-1``      for integers
  * ``-1.0``    for floating point numbers
  * ``'-'``     for characters
  * ``'-1'``    for strings
  * ``True``    for boolean values
* XXX: I just obtained these values empirically
- `join_by` (ID: 93d8ede5-ac20-45d7-a3d1-e5136ecc9e00): Join arrays `r1` and `r2` on key `key`.

The key should be either a string or a sequence of string corresponding
to the fields used to join the array.  An exception is raised if the
`key` field cannot be found in the two input arrays.  Neither `r1` nor
`r2` should have any duplicates along `key`: the presence of duplicates
will make the output quite unreliable. Note that duplicates are not
looked for by the algorithm.

Parameters
----------
key : {string, sequence}
    A string or a sequence of strings corresponding to the fields used
    for comparison.
r1, r2 : arrays
    Structured arrays.
jointype : {'inner', 'outer', 'leftouter'}, optional
    If 'inner', returns the elements common to both r1 and r2.
    If 'outer', returns the common elements as well as the elements of
    r1 not in r2 and the elements of not in r2.
    If 'leftouter', returns the common elements and the elements of r1
    not in r2.
r1postfix : string, optional
    String appended to the names of the fields of r1 that are present
    in r2 but absent of the key.
r2postfix : string, optional
    String appended to the names of the fields of r2 that are present
    in r1 but absent of the key.
defaults : {dictionary}, optional
    Dictionary mapping field names to the corresponding default values.
usemask : {True, False}, optional
    Whether to return a MaskedArray (or MaskedRecords is
    `asrecarray==True`) or a ndarray.
asrecarray : {False, True}, optional
    Whether to return a recarray (or MaskedRecords if `usemask==True`)
    or just a flexible-type ndarray.

Notes
-----
* The output is sorted along the key.
* A temporary array is formed by dropping the fields not in the key for
  the two arrays and concatenating the result. This array is then
  sorted, and the common entries selected. The output is constructed by
  filling the fields with the selected entries. Matching is not
  preserved if there are some duplicates...
- `get_names_flat` (ID: 4571f34a-d8a6-4ddf-b023-1558820fa88c): Returns the field names of the input datatype as a tuple. Input datatype
must have fields otherwise error is raised.
Nested structure are flattened beforehand.

Parameters
----------
adtype : dtype
    Input datatype

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> rfn.get_names_flat(np.empty((1,), dtype=[('A', int)]).dtype) is None
False
>>> rfn.get_names_flat(np.empty((1,), dtype=[('A',int), ('B', str)]).dtype)
('A', 'B')
>>> adtype = np.dtype([('a', int), ('b', [('ba', int), ('bb', int)])])
>>> rfn.get_names_flat(adtype)
('a', 'b', 'ba', 'bb')
- `get_names` (ID: 98ea3ee2-929c-42ad-ba9a-58f953b9bd85): Returns the field names of the input datatype as a tuple. Input datatype
must have fields otherwise error is raised.

Parameters
----------
adtype : dtype
    Input datatype

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> rfn.get_names(np.empty((1,), dtype=[('A', int)]).dtype)
('A',)
>>> rfn.get_names(np.empty((1,), dtype=[('A',int), ('B', float)]).dtype)
('A', 'B')
>>> adtype = np.dtype([('a', int), ('b', [('ba', int), ('bb', int)])])
>>> rfn.get_names(adtype)
('a', ('b', ('ba', 'bb')))
- `get_fieldstructure` (ID: 4a29f875-2ce6-4b46-8779-ece3eebcd221): Returns a dictionary with fields indexing lists of their parent fields.

This function is used to simplify access to fields nested in other fields.

Parameters
----------
adtype : np.dtype
    Input datatype
lastname : optional
    Last processed field name (used internally during recursion).
parents : dictionary
    Dictionary of parent fields (used internally during recursion).

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> ndtype =  np.dtype([('A', int),
...                     ('B', [('BA', int),
...                            ('BB', [('BBA', int), ('BBB', int)])])])
>>> rfn.get_fieldstructure(ndtype)
... # XXX: possible regression, order of BBA and BBB is swapped
{'A': [], 'B': [], 'BA': ['B'], 'BB': ['B'], 'BBA': ['B', 'BB'], 'BBB': ['B', 'BB']}
- `flatten_descr` (ID: d9544766-ec97-4b93-adad-d20f8ee27ff8): Flatten a structured data-type description.

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> ndtype = np.dtype([('a', '<i4'), ('b', [('ba', '<f8'), ('bb', '<i4')])])
>>> rfn.flatten_descr(ndtype)
(('a', dtype('int32')), ('ba', dtype('float64')), ('bb', dtype('int32')))
- `find_duplicates` (ID: 27d2acbb-7319-47fd-ac81-0e6e3544c191): Find the duplicates in a structured array along a given key

Parameters
----------
a : array-like
    Input array
key : {string, None}, optional
    Name of the fields along which to check the duplicates.
    If None, the search is performed by records
ignoremask : {True, False}, optional
    Whether masked data should be discarded or considered as duplicates.
return_index : {False, True}, optional
    Whether to return the indices of the duplicated values.

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> ndtype = [('a', int)]
>>> a = np.ma.array([1, 1, 1, 2, 2, 3, 3],
...         mask=[0, 0, 1, 0, 0, 0, 1]).view(ndtype)
>>> rfn.find_duplicates(a, ignoremask=True, return_index=True)
(masked_array(data=[(1,), (1,), (2,), (2,)],
             mask=[(False,), (False,), (False,), (False,)],
       fill_value=(999999,),
            dtype=[('a', '<i8')]), array([0, 1, 3, 4]))
- `drop_fields` (ID: e00da075-1ed3-4a0f-ae54-3e8f463779aa): Return a new array with fields in `drop_names` dropped.

Nested fields are supported.

Parameters
----------
base : array
    Input array
drop_names : string or sequence
    String or sequence of strings corresponding to the names of the
    fields to drop.
usemask : {False, True}, optional
    Whether to return a masked array or not.
asrecarray : string or sequence, optional
    Whether to return a recarray or a mrecarray (`asrecarray=True`) or
    a plain ndarray or masked array with flexible dtype. The default
    is False.

Examples
--------
>>> import numpy as np
>>> from numpy.lib import recfunctions as rfn
>>> a = np.array([(1, (2, 3.0)), (4, (5, 6.0))],
...   dtype=[('a', np.int64), ('b', [('ba', np.double), ('bb', np.int64)])])
>>> rfn.drop_fields(a, 'a')
array([((2., 3),), ((5., 6),)],
      dtype=[('b', [('ba', '<f8'), ('bb', '<i8')])])
>>> rfn.drop_fields(a, 'ba')
array([(1, (3,)), (4, (6,))], dtype=[('a', '<i8'), ('b', [('bb', '<i8')])])
>>> rfn.drop_fields(a, ['ba', 'bb'])
array([(1,), (4,)], dtype=[('a', '<i8')])
- `assign_fields_by_name` (ID: 5bd9539f-11b3-4121-a94a-254ccddd03b4): Assigns values from one structured array to another by field name.

Normally in numpy >= 1.14, assignment of one structured array to another
copies fields "by position", meaning that the first field from the src is
copied to the first field of the dst, and so on, regardless of field name.

This function instead copies "by field name", such that fields in the dst
are assigned from the identically named field in the src. This applies
recursively for nested structures. This is how structure assignment worked
in numpy >= 1.6 to <= 1.13.

Parameters
----------
dst : ndarray
src : ndarray
    The source and destination arrays during assignment.
zero_unassigned : bool, optional
    If True, fields in the dst for which there was no matching
    field in the src are filled with the value 0 (zero). This
    was the behavior of numpy <= 1.13. If False, those fields
    are not modified.
- `apply_along_fields` (ID: aef5151c-f307-40c4-a1aa-1a8ab049a3f0): Apply function 'func' as a reduction across fields of a structured array.

This is similar to `numpy.apply_along_axis`, but treats the fields of a
structured array as an extra axis. The fields are all first cast to a
common type following the type-promotion rules from `numpy.result_type`
applied to the field's dtypes.

Parameters
----------
func : function
   Function to apply on the "field" dimension. This function must
   support an `axis` argument, like `numpy.mean`, `numpy.sum`, etc.
arr : ndarray
   Structured array for which to apply func.

Returns
-------
out : ndarray
   Result of the reduction operation

Examples
--------
>>> import numpy as np

>>> from numpy.lib import recfunctions as rfn
>>> b = np.array([(1, 2, 5), (4, 5, 7), (7, 8 ,11), (10, 11, 12)],
...              dtype=[('x', 'i4'), ('y', 'f4'), ('z', 'f8')])
>>> rfn.apply_along_fields(np.mean, b)
array([ 2.66666667,  5.33333333,  8.66666667, 11.        ])
>>> rfn.apply_along_fields(np.mean, b[['x', 'z']])
array([ 3. ,  5.5,  9. , 11. ])
- `append_fields` (ID: a2fb392b-07d0-4d6c-9913-9910d8db9ca7): Add new fields to an existing array.

The names of the fields are given with the `names` arguments,
the corresponding values with the `data` arguments.
If a single field is appended, `names`, `data` and `dtypes` do not have
to be lists but just values.

Parameters
----------
base : array
    Input array to extend.
names : string, sequence
    String or sequence of strings corresponding to the names
    of the new fields.
data : array or sequence of arrays
    Array or sequence of arrays storing the fields to add to the base.
dtypes : sequence of datatypes, optional
    Datatype or sequence of datatypes.
    If None, the datatypes are estimated from the `data`.
fill_value : {float}, optional
    Filling value used to pad missing data on the shorter arrays.
usemask : {False, True}, optional
    Whether to return a masked array or not.
asrecarray : {False, True}, optional
    Whether to return a recarray (MaskedRecords) or not.
- `opt_func_info` (ID: 638bd712-67c1-4a3e-b401-bdfc19ed3ac5): Returns a dictionary containing the currently supported CPU dispatched
features for all optimized functions.

Parameters
----------
func_name : str (optional)
    Regular expression to filter by function name.

signature : str (optional)
    Regular expression to filter by data type.

Returns
-------
dict
    A dictionary where keys are optimized function names and values are
    nested dictionaries indicating supported targets based on data types.

Examples
--------
Retrieve dispatch information for functions named 'add' or 'sub' and
data types 'float64' or 'float32':

>>> import numpy as np
>>> dict = np.lib.introspect.opt_func_info(
...     func_name="add|abs", signature="float64|complex64"
... )
>>> import json
>>> print(json.dumps(dict, indent=2))   # may vary (architecture)
    {
      "absolute": {
        "dd": {
          "current": "SSE41",
          "available": "SSE41 baseline(SSE SSE2 SSE3)"
        },
        "Ff": {
          "current": "FMA3__AVX2",
          "available": "AVX512F FMA3__AVX2 baseline(SSE SSE2 SSE3)"
        },
        "Dd": {
          "current": "FMA3__AVX2",
          "available": "AVX512F FMA3__AVX2 baseline(SSE SSE2 SSE3)"
        }
      },
      "add": {
        "ddd": {
          "current": "FMA3__AVX2",
          "available": "FMA3__AVX2 baseline(SSE SSE2 SSE3)"
        },
        "FFF": {
          "current": "FMA3__AVX2",
          "available": "FMA3__AVX2 baseline(SSE SSE2 SSE3)"
        }
      }
    }
- `test_irfft_with_n_large_regression` (ID: f69e505b-fa7d-4275-ab94-253e263ccd93): No description
- `test_irfft_with_n_1_regression` (ID: 07cf6c97-f707-4c09-a390-842d7dab16f5): No description
- `test_fft_with_order` (ID: 762245c4-8b92-46e6-b708-6e99c4d64292): No description
- `test_fft_with_integer_or_bool_input` (ID: 95eb3c14-fa40-4b2b-8a97-264943094e68): No description
- `test_fft_output_order` (ID: 3d062a6f-84ad-4789-b71f-8df289b53b2c): No description
- `fft1` (ID: 80cd8852-1b99-48f1-b2c0-7cf3560e4222): No description
- `rfftfreq` (ID: bacad968-a314-48cf-a9d5-943b9f808c07): No description
- `ifftshift` (ID: 56962928-63d6-4f1f-9e0d-b61ca0a4b3a2): No description
- `fftshift` (ID: 92856295-29ca-4f2b-aa7a-50e0bb163f84): No description
- `fftfreq` (ID: 0be00714-7d8c-4c8a-9fe5-efb40834e6a6): No description
- `buildusevars` (ID: a1c76044-9669-44bc-a46f-5959b91773f8): No description
- `buildusevar` (ID: 60074d32-4cff-4b97-943e-3716faaa4c44): No description
- `switchdir` (ID: de1e529e-edbd-4054-b20d-5f3102c76b24): No description
- `has_fortran_compiler` (ID: 6aa0fefb-9ea8-4dcd-9c0c-ea59b7929851): No description
- `has_f90_compiler` (ID: 506d2381-de60-4cce-b958-eaa4fd4c25ea): No description
- `has_f77_compiler` (ID: 27be3cfe-ce12-43c1-ae40-f3a7366bb52b): No description
- `has_c_compiler` (ID: 0b542dac-ef0d-49da-930f-e370e41b2353): No description
- `getpath` (ID: b3833f79-9205-48d6-a3b9-2e2701d84310): No description
- `get_temp_module_name` (ID: cfdd2f10-18ba-449b-b68d-382c9b6e59a8): No description
- `get_module_dir` (ID: 726a100b-b602-4705-b75f-42913c9c359b): No description
- `check_language` (ID: bf0dbb05-ab23-413b-b47c-3315f83a2720): No description
- `build_module` (ID: 9c706f5b-bbcb-4ca9-87dd-5f18913ea65b): Compile and import a f2py module, built from the given files.
- `build_meson` (ID: 4e2ca3cb-1980-4427-bbfc-86ca0b583dee): Build a module via Meson and import it.
- `build_code` (ID: b737de26-e4b9-407d-bd55-e725d06fcafc): Compile and import Fortran code using f2py.
- `test_include_path` (ID: 5e1f68e0-e3a6-48b2-972a-6d3f985bfba0): No description
- `test_gh26623` (ID: 55df6196-a973-42ae-bb38-ecb891c078b9): No description
- `test_gh25784` (ID: b2f15ed1-6780-4e7d-a087-e814a137c2de): No description
- `test_from_template` (ID: 41adb97f-294c-4c03-9d29-8f1c7a62f889): Regression test for gh-10712.
- `normalize_whitespace` (ID: fee8ce99-1694-4beb-b9f1-dd9fa4acb936): Remove leading and trailing whitespace, and convert internal
stretches of whitespace to a single space.
- `test_process_f2cmap_dict` (ID: acc6652a-8b1f-48e9-9c76-39b331576914): No description
- `test_wrapfunc_def` (ID: 86f7c89c-db20-4809-bd1e-0d4d8f22a9a7): Ensures that fortran subroutine wrappers for F77 are included by default

CLI :: --[no]-wrap-functions
- `test_version` (ID: 0a6ea1b7-829e-4e78-a8a6-5e4661b31bbd): Ensure version

CLI :: -v
- `test_verbose` (ID: 173b5fdf-1d83-47da-bfbf-84433de7e4a9): Increase verbosity

CLI :: --verbose
- `test_untitled_cli` (ID: d1b456ed-44a8-4284-9f8c-e5de44932b05): Check that modules are named correctly

CLI :: defaults
- `test_shortlatex` (ID: 9981b183-c9ec-402d-8992-5ed3c39140f1): Ensures that truncated documentation is written out

TODO: Test to ensure this has no effect without --latex-doc
CLI :: --latex-doc --short-latex
- `test_restdoc` (ID: 27c76298-0292-4376-aa83-acd13eeb4369): Ensures that RsT documentation is written out

CLI :: --rest-doc
- `test_quiet` (ID: c4da02a6-27e6-4a6e-bd80-e7f016d6b2f3): Reduce verbosity

CLI :: --quiet
- `test_overwrite` (ID: 308e5de0-ecbe-41dc-8cee-c494c06fa1e0): Ensures that the build directory can be specified

CLI :: --overwrite-signature
- `test_npdistop` (ID: 6a2f25c2-ce6c-40a9-8f9f-2dff68fab7bf): CLI :: -c
- `test_npd_undefine` (ID: f941ffbb-8219-45c2-8ee3-9ada82297dde): CLI :: -U<name>
- `test_npd_opt` (ID: e67ca465-0e12-4e5d-8530-9fb5983f2096): CLI :: -c --opt
- `test_npd_noopt` (ID: 6a8725c6-1afb-407c-bb4c-c7175c583601): CLI :: -c --noopt
- `test_npd_noarch` (ID: 3b3a7d67-53a5-4a5c-a0f8-c63b7e630e82): CLI :: -c --noarch
- `test_npd_linker` (ID: 688c2c69-f296-43af-a6a0-5fa3f312a5ff): CLI :: <filename>.o <filename>.so <filename>.a
- `test_npd_link_auto` (ID: 61988bbd-6ea9-4eac-9654-8825860fa91d): CLI :: -c --link-<resource>
- `test_npd_lib` (ID: c36c95fa-15be-4f44-978c-3553f442083e): CLI :: -c -L/path/to/lib/ -l<libname>
- `test_npd_incl` (ID: 220b3879-4d8e-4192-ac52-2fde2fac3604): CLI :: -I/path/to/include/
- `test_npd_help_fcompiler` (ID: 430879c6-9f24-4b38-81b4-0b9ca5ba3d0a): CLI :: -c --help-fcompiler
- `test_npd_fcompiler` (ID: 970578da-e28a-4312-a2cc-072871ed2425): CLI :: -c --fcompiler
- `test_npd_f90flags` (ID: d7960244-d958-4f1c-98a5-12e50dd7f791): CLI :: -c --f90flags
- `test_npd_f90exec` (ID: aa57541e-c15b-4143-89d6-edf3caa16959): CLI :: -c --f90exec
- `test_npd_f77flags` (ID: 4a78dcf7-ef6f-47de-8306-a510edc3dff3): CLI :: -c --f77flags
- `test_npd_f77exec` (ID: aeddb5c9-48df-4eef-b19f-210a69b751cd): CLI :: -c --f77exec
- `test_npd_define` (ID: 8b6a133d-d31c-4258-b9a5-83ac00acc949): CLI :: -D<define>
- `test_npd_debug` (ID: 31cdb4b3-37dd-4028-a1ad-1e10f9cb5374): CLI :: -c --debug
- `test_npd_compiler` (ID: 5bac75b2-c7e5-4b84-b871-cc3afed54689): CLI :: -c --compiler
- `test_npd_arch` (ID: 663ec49e-c4a8-4178-bdd9-c4bd45a0e7b5): CLI :: -c --arch
- `test_nowrapfunc` (ID: eddfc58b-c8a8-456a-80c7-a64dc61bb7ad): Ensures that fortran subroutine wrappers for F77 can be disabled

CLI :: --no-wrap-functions
- `test_norestexdoc` (ID: 4ddd7ecb-3103-4643-951f-b455f049103c): Ensures that TeX documentation is written out

CLI :: --no-rest-doc
- `test_nolatexdoc` (ID: 83eb55e6-41c3-46eb-a4ca-c7fc32ae95a0): Ensures that TeX documentation is written out

CLI :: --no-latex-doc
- `test_no_py312_distutils_fcompiler` (ID: f8f72ca0-4758-4631-a22f-b581d670bbbf): Check that no distutils imports are performed on 3.12
CLI :: --fcompiler --help-link --backend distutils
- `test_no_freethreading_compatible` (ID: 4b9e5e8d-cc1b-4ddf-9dfa-43390987c6e4): CLI :: --no-freethreading-compatible
- `test_mod_gen_gh25263` (ID: 5dfabb8e-24b5-45c5-9d88-e5e245f84ca7): Check that pyf files are correctly generated with module structure
CLI :: -m <name> -h pyf_file
BUG: numpy-gh #20520
- `test_mod_gen_f77` (ID: 9e20ac25-cebd-45fc-8c2d-4750e8dfe408): Checks the generation of files based on a module name
CLI :: -m
- `test_lower_sig` (ID: 0d674006-2255-4daa-aba6-b02932be886a): Lowers cases in signature files by flag or when -h is present

CLI :: --[no-]lower -h
- `test_lower_cmod` (ID: 2737c3e3-795d-4347-a156-979009c9f0fd): Lowers cases by flag or when -h is present

CLI :: --[no-]lower
- `test_latexdoc` (ID: 4e2dc3d2-81a1-4d06-aeff-bdec3070c18c): Ensures that TeX documentation is written out

CLI :: --latex-doc
- `test_inclpath` (ID: 722b2e14-fb23-417c-90f0-9ad6f675c872): Add to the include directories

CLI :: --include-paths
- `test_inclheader` (ID: b4d846af-c4f4-4b6b-ad74-6e84bd1966af): Add to the include directories

CLI :: -include
TODO: Document this in the help string
- `test_hlink` (ID: a9748d47-7ebd-4e15-81d8-825e509eab97): Add to the include directories

CLI :: --help-link
- `test_gh23598_warn` (ID: 1a1d4431-e74a-46f9-a9fd-f1ee5c39eb79): No description
- `test_gh22819_many_pyf` (ID: 2f68bc01-be9c-4d39-a308-1751284f99ca): Only one .pyf file allowed
gh-22819
CLI :: .pyf files
- `test_gh22819_cli` (ID: 41ac82d7-ac72-47e4-84ad-27b252764875): Check that module names are handled correctly
gh-22819
Essentially, the -m name cannot be used to import the module, so the module
named in the .pyf needs to be used instead

CLI :: -m and a .pyf file
- `test_gen_pyf_stdout` (ID: 897d4362-3c44-4202-a685-aa632d973061): Ensures that a signature file can be dumped to stdout
CLI :: -h
- `test_gen_pyf_no_overwrite` (ID: eb455ac5-a889-4ee1-a12e-cc7d1f6d4043): Ensures that the CLI refuses to overwrite signature files
CLI :: -h without --overwrite-signature
- `test_gen_pyf` (ID: 7902e729-0ddc-4d1a-be2b-edcaa61d9731): Ensures that a signature file is generated via the CLI
CLI :: -h
- `test_freethreading_compatible` (ID: a7b0855e-6993-4f05-9768-37ea417c5a4b): CLI :: --freethreading_compatible
- `test_file_processing_switch` (ID: 988ccb51-45db-441e-b2c6-8c49012ca4a1): Tests that it is possible to return to file processing mode
CLI :: :
BUG: numpy-gh #20520
- `test_f2py_skip` (ID: 16566750-db12-4404-9fe1-219501a62a0d): Tests that functions can be skipped
CLI :: skip:
- `test_f2py_only` (ID: 31615bd7-d434-45d3-af94-5c1bc792397e): Test that functions can be kept by only:
CLI :: only:
- `test_f2cmap` (ID: cbe8dc84-82e6-427b-aab6-904d8e612562): Check that Fortran-to-Python KIND specs can be passed

CLI :: --f2cmap
- `test_debugcapi_bld` (ID: 56662f5d-83b1-420c-9304-15793eb773f9): Ensures that debugging wrappers work

CLI :: --debug-capi -c
- `test_debugcapi` (ID: 6e7498d1-6898-4175-9ca0-357725a14c50): Ensures that debugging wrappers are written

CLI :: --debug-capi
- `test_build_dir` (ID: f60a61aa-b13b-403f-87fb-32b39a97013b): Ensures that the build directory can be specified

CLI :: --build-dir
- `retreal_f77` (ID: 4fe2b499-9c5b-4be9-a590-f5ad5f9ca662): Generates a single f77 file for testing
- `hello_world_f90` (ID: cd133ff1-ddf4-43f1-a3d9-fdb7c2c7607b): Generates a single f90 file for testing
- `hello_world_f77` (ID: 8d732c45-b3e7-473c-aca5-2a07e1cba4da): Generates a single f77 file for testing
- `gh23598_warn` (ID: 6b24881e-124d-40e4-b172-58ae02217b22): F90 file for testing warnings in gh23598
- `gh22819_cli` (ID: 00105e43-c95c-4f89-9d6f-48b8776db44f): F90 file for testing disallowed CLI arguments in ghff819
- `get_io_paths` (ID: 5ff596a0-639b-4078-bfde-7c0b0a1fcd26): Takes in a temporary file for testing and returns the expected output and input paths

Here expected output is essentially one of any of the possible generated
files.

..note::

     Since this does not actually run f2py, none of these are guaranteed to
     exist, and module names are typically incorrect

Parameters
----------
fname_inp : str
            The input filename
mname : str, optional
            The name of the module, untitled by default

Returns
-------
genp : NamedTuple PPaths
        The possible paths which are generated, not all of which exist
- `f2cmap_f90` (ID: 92032b67-76a3-486e-a5e3-9ec55a644b1c): Generates a single f90 file for testing
- `compiler_check_f2pycli` (ID: 249f1a20-3ca2-43b3-8d7b-81ce4de7781a): No description
- `get_docdir` (ID: 3e32fbdc-897e-42c4-8617-24c75c2cbe72): No description
- `setup_module` (ID: 7158e4a8-ee97-40a9-a8d5-8c37cb7d932c): Build the required testing extension module
- `get_testdir` (ID: a6b9b1bd-19c5-48b6-8d90-083fd9171197): No description
- `flags_info` (ID: e760b21f-160f-4551-97db-cefd111f7d89): No description
- `flags2names` (ID: ac7db57b-ff1d-4770-845c-fa9ce5bcc902): No description
- `buildmodule` (ID: 6839670b-48a9-46f1-a11e-c3e4d673c304): Return
- `buildapi` (ID: 35908cb1-6804-4376-9ec1-283b0d285f8e): No description
- `get_include` (ID: 69712d53-f8d3-4839-90b8-0225f12b7252): Return the directory that contains the ``fortranobject.c`` and ``.h`` files.

.. note::

    This function is not needed when building an extension with
    `numpy.distutils` directly from ``.f`` and/or ``.pyf`` files
    in one go.

Python extension modules built with f2py-generated code need to use
``fortranobject.c`` as a source file, and include the ``fortranobject.h``
header. This function can be used to obtain the directory containing
both of these files.

Returns
-------
include_path : str
    Absolute path to the directory containing ``fortranobject.c`` and
    ``fortranobject.h``.

Notes
-----
.. versionadded:: 1.21.1

Unless the build system you are using has specific support for f2py,
building a Python extension using a ``.pyf`` signature file is a two-step
process. For a module ``mymod``:

* Step 1: run ``python -m numpy.f2py mymod.pyf --quiet``. This
  generates ``mymodmodule.c`` and (if needed)
  ``mymod-f2pywrappers.f`` files next to ``mymod.pyf``.
* Step 2: build your Python extension module. This requires the
  following source files:

  * ``mymodmodule.c``
  * ``mymod-f2pywrappers.f`` (if it was generated in Step 1)
  * ``fortranobject.c``

See Also
--------
numpy.get_include : function that returns the numpy include directory
- `var2fixfortran` (ID: 1e447763-8926-4752-92d7-a412c62455c1): No description
- `useiso_c_binding` (ID: 891615c9-6fb1-44d9-9b6d-d9b1fd47263a): No description
- `createsubrwrapper` (ID: 9cd163fd-98fe-4c10-949a-954fcd07eaca): No description
- `createfuncwrapper` (ID: de344b71-76e1-4f43-aa96-9937a13314a3): No description
- `assubr` (ID: 2314010c-f627-4ae9-b744-a6e793254e92): No description
- `findf90modules` (ID: 27a9fcec-8d24-469e-bfd3-14a59a5bf6c2): No description
- `buildhooks` (ID: d1a5bf37-c8a6-4042-be9f-6b3243b9440d): No description
- `validate_modulename` (ID: c6154182-46dc-4e95-a587-5af4db5f5484): No description
- `scaninputline` (ID: 7aa2295d-5641-4cd0-875c-b9b6126786a0): No description
- `run_main` (ID: bce1a4f6-83b0-4374-acce-450c39a30a86): Equivalent to running::

    f2py <args>

where ``<args>=string.join(<list>,' ')``, but in Python.  Unless
``-h`` is used, this function returns a dictionary containing
information on generated modules and their dependencies on source
files.

You cannot build extension modules with this function, that is,
using ``-c`` is not allowed. Use the ``compile`` command instead.

Examples
--------
The command ``f2py -m scalar scalar.f`` can be executed from Python as
follows.

.. literalinclude:: ../../source/f2py/code/results/run_main_session.dat
    :language: python
- `run_compile` (ID: 4a26592f-4e52-45f4-9801-8506d7fd7be6): Do it all in one call!
- `preparse_sysargv` (ID: 436aa16b-b5a4-4e71-ba57-6b0c7193c595): No description
- `make_f2py_compile_parser` (ID: d317dcad-b4b6-463f-bedb-f492433ae032): No description
- `main` (ID: b67c0286-551a-462d-859a-c25573fd5143): No description
- `get_prefix` (ID: 6d9b3a2b-4400-4561-8e7d-664fb873cd78): No description
- `get_newer_options` (ID: 88951465-5566-44a3-90c1-3a10cf2afd99): No description
- `filter_files` (ID: ffd98f13-ca8f-4c8a-a603-4f5c901dd9db): Filter files by prefix and suffix.
- `f2py_parser` (ID: b9d43cdc-6051-47b1-863d-f0339c7dad49): No description
- `dict_append` (ID: 6964b93b-7a6c-404d-bb05-8e45410cbaa8): No description
- `callcrackfortran` (ID: be0ae46e-1bcd-4535-bf3a-296d3141bcf4): No description
- `buildmodules` (ID: 7dfd8398-5c75-4ad6-8760-e7a3f42c4de1): No description
- `run` (ID: 869ce1ea-5f61-4495-8a42-b7cfe8ae4e31): No description
- `vars2fortran` (ID: 6e055991-6e57-4224-9483-be545cff6820): No description
- `use2fortran` (ID: 1d5c191c-ba97-48aa-a798-ef807ae4d888): No description
- `updatevars` (ID: a639fb68-89de-4ba6-aecf-ca18fb7cb0ac): Returns last_name, the variable name without special chars, parenthesis
    or dimension specifiers.

Alters groupcache to add the name, typespec, attrspec (and possibly value)
of current variable.
- `unmarkouterparen` (ID: 9fa3f13a-22da-4e9c-a1b3-a182ddc2bc29): No description
- `undo_rmbadname1` (ID: 4522bfb0-26c6-4393-9070-a4790778a6ff): No description
- `undo_rmbadname` (ID: e87520e0-67fb-4588-9daf-dee3d69a15b9): No description
- `true_intent_list` (ID: 1cd66f52-13b1-48ee-a263-80ddf9cb903f): No description
- `traverse` (ID: bff0e4ab-3b7d-4710-addd-8ef84d508649): Traverse f2py data structure with the following visit function:

def visit(item, parents, result, *args, **kwargs):
    """

    parents is a list of key-"f2py data structure" pairs from which
    items are taken from.

    result is a f2py data structure that is filled with the
    return value of the visit function.

    item is 2-tuple (index, value) if parents[-1][1] is a list
    item is 2-tuple (key, value) if parents[-1][1] is a dict

    The return value of visit must be None, or of the same kind as
    item, that is, if parents[-1] is a list, the return value must
    be 2-tuple (new_index, new_value), or if parents[-1] is a
    dict, the return value must be 2-tuple (new_key, new_value).

    If new_index or new_value is None, the return value of visit
    is ignored, that is, it will not be added to the result.

    If the return value is None, the content of obj will be
    traversed, otherwise not.
    """
- `split_by_unquoted` (ID: 5dc09d43-17e9-4e0a-a2bc-0df16465b2d7): Splits the line into (line[:i], line[i:]),
where i is the index of first occurrence of one of the characters
not within quotes, or len(line) if no such index exists
- `sortvarnames` (ID: f1448920-a60f-4498-bab5-ad84dea01fa4): No description
- `setmesstext` (ID: 12d1485e-31c8-4cd1-b64d-c0de9989d021): No description
- `setkindselector` (ID: beb43755-10e2-442d-aecf-7be20d05e204): No description
- `setcharselector` (ID: 99c02b52-8312-4c17-bc01-eadfc2eb668b): No description
- `setattrspec` (ID: e56a921a-5cd9-4ca5-a419-c566685de761): No description
- `rmbadname1` (ID: 2a52c116-e42b-4637-9a7c-edd1f093420f): No description
- `rmbadname` (ID: 0a2611fa-c288-4cc3-b621-a2074c792cf0): No description
- `reset_global_f2py_vars` (ID: 9db53060-c0af-4dba-8f02-92e0ddcd0d2d): No description
- `removespaces` (ID: 45ff0011-30c9-40c3-aff5-6d1d2977ab23): No description
- `readfortrancode` (ID: 6cdaf06d-f5af-4bc1-befd-8a1dc484b72a): Read fortran codes from files and
 1) Get rid of comments, line continuations, and empty lines; lower cases.
 2) Call dowithline(line) on every line.
 3) Recursively call itself when statement "include '<filename>'" is met.
- `postcrack2` (ID: d26f3dc4-6753-41a3-bdb9-f19147914632): No description
- `postcrack` (ID: 74470dfb-2998-49c7-8bb3-4775e111d98d): TODO:
      function return values
      determine expression types if in argument list
- `parse_name_for_bind` (ID: b54f7c49-6697-4b2a-b743-44aec73255aa): No description
- `param_parse` (ID: 66f484c4-6c4d-4b1d-bb9a-7703e499538c): Recursively parse array dimensions.

Parses the declaration of an array variable or parameter
`dimension` keyword, and is called recursively if the
dimension for this array is a previously defined parameter
(found in `params`).

Parameters
----------
d : str
    Fortran expression describing the dimension of an array.
params : dict
    Previously parsed parameters declared in the Fortran source file.

Returns
-------
out : str
    Parsed dimension expression.

Examples
--------

* If the line being analyzed is

  `integer, parameter, dimension(2) :: pa = (/ 3, 5 /)`

  then `d = 2` and we return immediately, with

>>> d = '2'
>>> param_parse(d, params)
2

* If the line being analyzed is

  `integer, parameter, dimension(pa) :: pb = (/1, 2, 3/)`

  then `d = 'pa'`; since `pa` is a previously parsed parameter,
  and `pa = 3`, we call `param_parse` recursively, to obtain

>>> d = 'pa'
>>> params = {'pa': 3}
>>> param_parse(d, params)
3

* If the line being analyzed is

  `integer, parameter, dimension(pa(1)) :: pb = (/1, 2, 3/)`

  then `d = 'pa(1)'`; since `pa` is a previously parsed parameter,
  and `pa(1) = 3`, we call `param_parse` recursively, to obtain

>>> d = 'pa(1)'
>>> params = dict(pa={1: 3, 2: 5})
>>> param_parse(d, params)
3
- `param_eval` (ID: 8826acd2-837b-43c7-aefb-3681f22a9bf1): Creates a dictionary of indices and values for each parameter in a
parameter array to be evaluated later.

WARNING: It is not possible to initialize multidimensional array
parameters e.g. dimension(-3:1, 4, 3:5) at this point. This is because in
Fortran initialization through array constructor requires the RESHAPE
intrinsic function. Since the right-hand side of the parameter declaration
is not executed in f2py, but rather at the compiled c/fortran extension,
later, it is not possible to execute a reshape of a parameter array.
One issue remains: if the user wants to access the array parameter from
python, we should either
1) allow them to access the parameter array using python standard indexing
   (which is often incompatible with the original fortran indexing)
2) allow the parameter array to be accessed in python as a dictionary with
   fortran indices as keys
We are choosing 2 for now.
- `outmess` (ID: 5727a7b3-2ea3-4a27-9377-a4be9164156c): No description
- `openhook` (ID: 6079ef14-0e18-425e-ae7b-263fa5017bb0): Ensures that filename is opened with correct encoding parameter.

This function uses charset_normalizer package, when available, for
determining the encoding of the file to be opened. When charset_normalizer
is not available, the function detects only UTF encodings, otherwise, ASCII
encoding is used as fallback.
- `myeval` (ID: 230e1856-b0ff-4017-9941-93f809b7010f): Like `eval` but returns only integers and floats
- `markouterparen` (ID: 917a4c26-14ab-42e2-9aeb-7cabb0de7e27): No description
- `markoutercomma` (ID: 3a396da6-544e-4edf-ab04-6455bf50dc0f): No description
- `markinnerspaces` (ID: b9178f83-6908-4e8d-84c6-7573cfe17926): The function replace all spaces in the input variable line which are
surrounded with quotation marks, with the triplet "@_@".

For instance, for the input "a 'b c'" the function returns "a 'b@_@c'"

Parameters
----------
line : str

Returns
-------
str
- `is_free_format` (ID: c364395d-fa26-4021-b08d-481984647f9a): Check if file is in free format Fortran.
- `getlincoef` (ID: 290427d6-5ae9-49a4-8d6a-a246a30dc4ed): Obtain ``a`` and ``b`` when ``e == "a*x+b"``, where ``x`` is a symbol in
xset.

>>> getlincoef('2*x + 1', {'x'})
(2, 1, 'x')
>>> getlincoef('3*x + x*2 + 2 + 1', {'x'})
(5, 3, 'x')
>>> getlincoef('0', {'x'})
(0, 0, None)
>>> getlincoef('0*x', {'x'})
(0, 0, 'x')
>>> getlincoef('x*x', {'x'})
(None, None, None)

This can be tricked by sufficiently complex expressions

>>> getlincoef('(x - 0.5)*(x - 1.5)*(x - 1)*x + 2*x + 3', {'x'})
(2.0, 3.0, 'x')
- `getblockname` (ID: 9736e267-e848-4109-b65c-e72c045ce521): No description
- `get_useparameters` (ID: a591f5f4-2371-4044-aa57-45ff0121c98c): No description
- `get_usedict` (ID: 501febc4-4575-4726-a575-17c7ebb55de8): No description
- `get_sorted_names` (ID: fcfa4b8a-5b28-49b5-915e-fa34371d5452): No description
- `get_parameters` (ID: 91ba6f61-da76-4199-bdd4-bc632226cf54): No description
- `expr2name` (ID: a041e2dc-4de0-4955-8c70-0eed458b8901): No description
- `determineexprtype` (ID: 89bbbee6-6bcf-4cd9-862b-ffd4add85be2): No description
- `cracktypespec0` (ID: 0ffa0e99-4d91-4c00-b870-f3b7d49ec472): No description
- `cracktypespec` (ID: 3fc88068-653a-4ffc-871d-f294c8bcd121): No description
- `crackline` (ID: 230a4a02-f6bf-48b5-82b3-11b59186b365): reset=-1  --- initialize
reset=0   --- crack the line
reset=1   --- final check if mismatch of blocks occurred

Cracked data is saved in grouplist[0].
- `crackfortran` (ID: 5bb20234-b523-45d6-afe8-e0eb3d04890b): No description
- `crack2fortrangen` (ID: cfcb876c-134c-4fc9-b45b-df46172637f1): No description
- `crack2fortran` (ID: 63e38e13-2db1-4e80-ae31-345b36547529): No description
- `common2fortran` (ID: 851afbd2-c4dc-4f6e-8dc9-e4063fb08826): No description
- `character_backward_compatibility_hook` (ID: d8655723-e773-4a98-b8b9-3b5f4ffedd70): Previously, Fortran character was incorrectly treated as
character*1. This hook fixes the usage of the corresponding
variables in `check`, `dimension`, `=`, and `callstatement`
expressions.

The usage of `char*` in `callprotoargument` expression can be left
unchanged because C `character` is C typedef of `char`, although,
new implementations should use `character*` in the corresponding
expressions.

See https://github.com/numpy/numpy/pull/19388 for more information.
- `buildimplicitrules` (ID: 769173d1-ae1d-4ed8-982d-d7ac5c8eb5f6): No description
- `appendmultiline` (ID: 69464604-777c-4ce9-b987-00d52c5f8805): No description
- `appenddecl` (ID: 8d95aa27-c0f4-472d-99bd-c39f854fcf7a): No description
- `analyzevars` (ID: 8385848f-c286-442f-96e7-03e0390e517a): Sets correct dimension information for each variable/parameter
- `analyzeline` (ID: 97aa0e86-26e6-4806-af0b-145a25d7113d): Reads each line in the input file in sequence and updates global vars.

Effectively reads and collects information from the input file to the
global variable groupcache, a dictionary containing info about each part
of the fortran module.

At the end of analyzeline, information is filtered into the correct dict
keys, but parameter values and dimensions are not yet interpreted.
- `analyzecommon` (ID: 1882af58-559b-4611-b520-c1b94fce79ae): No description
- `analyzebody` (ID: bd1ca2da-4b92-44e6-a9a0-a6903eb423e0): No description
- `analyzeargs` (ID: 7d5e1170-9bd1-4ebf-9320-594bdd3a8403): No description
- `findcommonblocks` (ID: 16b659f0-131e-4309-9635-4de1ce0e3341): No description
- `buildhooks` (ID: 3cc97b58-d1f5-4c38-bd3d-16b7807b6ec7): No description
- `get_needs` (ID: 7d5cc86c-b8ef-4f4d-9726-55e6925a57a3): No description
- `errmess` (ID: d98fea01-a3ff-4a89-ad53-9b4b9e701dec): Write an error message to stderr.

This indirection is needed because sys.stderr might not always be available (see #26862).
- `buildcfuncs` (ID: 8657c184-fa0b-4a64-a93e-b80d67f61800): No description
- `append_needs` (ID: a65953e5-a5c6-4951-95dd-1bf933b761b7): No description
- `buildcallbacks` (ID: 933fe9e4-cd07-4703-b7c5-9cf13c183ef5): No description
- `buildcallback` (ID: b1b639ea-d81d-4e9d-bff9-5f16a9182e1e): No description
- `sign2map` (ID: 19172f41-66df-4fbe-aa98-0375bbae482d): varname,ctype,atype
init,init.r,init.i,pytype
vardebuginfo,vardebugshowvalue,varshowvalue
varrformat

intent
- `routsign2map` (ID: f1b29d94-86aa-45c0-bcd4-7abb10610721): name,NAME,begintitle,endtitle
rname,ctype,rformat
routdebugshowvalue
- `modsign2map` (ID: c05bf39f-3b5d-4ecc-b9bd-30117aff85bd): modulename
- `getstrlength` (ID: 9e1716c9-f288-4e94-9b61-bdea6b7e387c): No description
- `getpydocsign` (ID: 5b008fec-bf35-48ea-b80e-7ed8fb637e39): No description
- `getinit` (ID: a2b1f2af-0c1e-4529-9ca9-3d20a8612342): No description
- `getctype` (ID: 20d894ae-d3b4-4c6d-bde6-9cc2bee9769d): Determines C type
- `getarrdocsign` (ID: f91ecb49-d708-48bb-ad5d-53cd614e0063): No description
- `getarrdims` (ID: 4d4a4b0d-0b51-404d-bab0-dd20ea1b9ad0): No description
- `common_sign2map` (ID: 3aba6dea-ad76-4b11-9a85-1ee1d944c9a0): No description
- `cb_sign2map` (ID: 32336aab-32a5-44c6-902d-ec5d04fcc489): No description
- `cb_routsign2map` (ID: ebc20951-cd04-4048-a191-cddbead94e5b): name,begintitle,endtitle,argname
ctype,rctype,maxnofargs,nofoptargs,returncptr
- `stripcomma` (ID: 1cce5e65-23f3-4f19-8e8a-4066408fa8ed): No description
- `replace` (ID: a81f937d-4714-45da-9829-63cfe8808850): No description
- `process_f2cmap_dict` (ID: bb5fbc65-0866-41ee-bbff-0ffb1c1f988d): Update the Fortran-to-C type mapping dictionary with new mappings and
return a list of successfully mapped C types.

This function integrates a new mapping dictionary into an existing
Fortran-to-C type mapping dictionary. It ensures that all keys are in
lowercase and validates new entries against a given C-to-Python mapping
dictionary. Redefinitions and invalid entries are reported with a warning.

Parameters
----------
f2cmap_all : dict
    The existing Fortran-to-C type mapping dictionary that will be updated.
    It should be a dictionary of dictionaries where the main keys represent
    Fortran types and the nested dictionaries map Fortran type specifiers
    to corresponding C types.

new_map : dict
    A dictionary containing new type mappings to be added to `f2cmap_all`.
    The structure should be similar to `f2cmap_all`, with keys representing
    Fortran types and values being dictionaries of type specifiers and their
    C type equivalents.

c2py_map : dict
    A dictionary used for validating the C types in `new_map`. It maps C
    types to corresponding Python types and is used to ensure that the C
    types specified in `new_map` are valid.

verbose : boolean
    A flag used to provide information about the types mapped

Returns
-------
tuple of (dict, list)
    The updated Fortran-to-C type mapping dictionary and a list of
    successfully mapped C types.
- `outmess` (ID: b223d092-b819-4155-bfd8-fb521dec6eda): No description
- `l_or` (ID: e6b52e1d-2008-4818-abcd-b7033528b619): No description
- `l_not` (ID: 0faca37d-d1f7-4f77-afd6-93ab1aa37c4e): No description
- `l_and` (ID: 4a4418a0-a822-43ac-b28e-205349a8232f): No description
- `isvariable` (ID: b306d630-2534-40df-9f7a-4333a65e70c4): No description
- `isunsigned_shortarray` (ID: cc2cb73d-3e4e-4a67-b422-e68c45a30d87): No description
- `isunsigned_short` (ID: 48ac9aec-8232-4b41-bbc3-29e5402db87f): No description
- `isunsigned_long_longarray` (ID: 3a690fc2-3cd5-4f05-a2e2-130581f18d7d): No description
- `isunsigned_long_long` (ID: 74d20225-ee55-4d3c-ad4d-c26711f607ad): No description
- `isunsigned_chararray` (ID: 5cdabc2d-0117-4914-96cd-c947dd57c044): No description
- `isunsigned_char` (ID: f5e233c0-bd6b-441c-bc2e-98dda54ddac1): No description
- `isunsigned` (ID: 5e1e6b4b-2dff-4e9d-9727-29e6942565cd): No description
- `isthreadsafe` (ID: 09652b69-ad6e-44be-9a8a-d478fa4cbad2): No description
- `issubroutine_wrap` (ID: afd3fa16-a24c-4045-8042-6c96dd15f82e): No description
- `issubroutine` (ID: a0e41714-141e-41b3-aa8f-e66be005765a): No description
- `isstringfunction` (ID: 973a1690-2336-4b5f-86f0-230be1302a85): No description
- `isstringarray` (ID: 2963c5d2-d971-42a0-a36b-9c1f08eb4329): No description
- `isstring_or_stringarray` (ID: e39b316f-e9b9-43b0-96b7-a14de8e9bee9): No description
- `isstring` (ID: 62732ed6-0624-4a75-b5e0-dae958d98564): No description
- `issigned_long_longarray` (ID: 72a1dc67-cdd3-4191-be3e-d95971390b46): No description
- `isscalar` (ID: ce077334-b719-4ac1-8588-1dbffa187b56): No description
- `isroutine` (ID: c6d54f05-7ae4-4893-a49b-9faf54d83ed5): No description
- `isrequired` (ID: 376b1b7f-7e52-448e-8eb6-4aa43aaa047f): No description
- `isprivate` (ID: 9163cf59-4507-41ea-8843-fd24db6f1b34): No description
- `isoptional` (ID: 09e94766-07e9-4cf4-ae7b-87602fc82a58): No description
- `ismoduleroutine` (ID: f25f7a83-50da-4bcf-a69a-d19005ba5fc1): No description
- `ismodule` (ID: e8816074-e1cc-40bb-8160-54ec4596e912): No description
- `islong_longfunction` (ID: 08b105be-a0f0-441f-9726-17df6b00ae5f): No description
- `islong_long` (ID: 46be5f05-56d8-434f-88c7-550f7f13ad60): No description
- `islong_doublefunction` (ID: a83bd3dc-9116-460b-a1d3-9ab972b216f9): No description
- `islong_double` (ID: 7a584efd-ce33-476d-a5d1-f7417b3710a5): No description
- `islong_complex` (ID: e697ab9b-f01d-4caa-8cdc-9e541f2950f9): No description
- `islogicalfunction` (ID: 36d61ee9-fcf8-4c1c-8ac8-2d572e2caaf4): No description
- `islogical` (ID: a0902842-1521-4d9c-8db2-2f96f7360bed): No description
- `isintent_overwrite` (ID: 435dbb53-c975-4144-80bd-5cc1723544da): No description
- `isintent_out` (ID: c24859a6-6d67-4fd9-affc-4abfc91a6f0c): No description
- `isintent_nothide` (ID: a8b2f911-a519-4536-9d5a-8ebf8a7bbbc4): No description
- `isintent_inplace` (ID: 701713ac-99b0-4d7d-8fe7-c6b25a43188f): No description
- `isintent_inout` (ID: 373749bd-5139-4d6d-a03b-00d226bb4306): No description
- `isintent_in` (ID: 92f1e575-1379-404d-903d-77e425ff33a8): No description
- `isintent_hide` (ID: 63f82fd9-0e67-4cb7-acde-f45c770c92a5): No description
- `isintent_copy` (ID: 0d93ca51-6f38-4d75-84b2-0022cd5db714): No description
- `isintent_callback` (ID: 0a4e8dca-b9de-4ce5-ab64-e0178f13cdad): No description
- `isintent_c` (ID: 8548b79c-f455-400d-b9ca-cdd6e0a75a43): No description
- `isintent_aux` (ID: 63b41b07-0613-41a5-b84a-6db0675b5dc4): No description
- `isinteger` (ID: 9cebd5c8-82e4-4769-ac96-59f2e5f85edf): No description
- `isint1array` (ID: 525564e6-373b-4d09-8a1b-bc4bbbcab805): No description
- `isint1` (ID: 9652a182-5481-46c9-b938-ea2cc220cd19): No description
- `isfunction_wrap` (ID: f86b3efc-bc60-46d9-a3df-12bbdcb4aced): No description
- `isfunction` (ID: f0130730-7a38-4b44-bc26-07f9df234529): No description
- `isexternal` (ID: 2af4496c-979d-4383-8edd-db5078d0087a): No description
- `isdummyroutine` (ID: 3fe9217c-b071-433e-8b5d-276add7052c4): No description
- `isdouble` (ID: da32d508-1481-454a-9bbe-8075335e8a75): No description
- `iscstyledirective` (ID: e96e5ba7-ac8d-4a50-8a7b-547084fbce17): No description
- `iscomplexfunction_warn` (ID: 588d200f-6a16-4cc4-bce8-747419395b79): No description
- `iscomplexfunction` (ID: d147c76f-9e50-4f24-960b-a1e6d3b61954): No description
- `iscomplexarray` (ID: 8c1c540b-dc9e-4b53-bf27-cc955349a041): No description
- `iscomplex` (ID: 0cc41a98-dc20-48be-91d2-302e189cc617): No description
- `ischaracterarray` (ID: 9dca3c6b-1586-419f-b1e5-b38f9c239ffc): No description
- `ischaracter_or_characterarray` (ID: 4411ee4a-fda6-4479-94ee-cc11a45d4c2c): No description
- `ischaracter` (ID: beb33557-4b0a-4b91-bac5-fd4b08ef1e20): No description
- `isattr_value` (ID: 285b700e-669e-42f1-a6ff-e4c56c9609ff): No description
- `isarrayofstrings` (ID: da65cbcf-9cc0-4104-b4e5-33167643cd68): No description
- `isarray` (ID: 0b6f364d-7c8e-47f7-a0fb-9f20d84a18e8): No description
- `isallocatable` (ID: 0af61fc2-1288-4fec-80c4-fa37edc436aa): No description
- `hasresultnote` (ID: ef610a34-1fe5-42fa-b55a-edd41e3f6c3d): No description
- `hasnote` (ID: 593eab37-c18e-42db-8129-e3295b18ca28): No description
- `hasinitvalue` (ID: 1c2410c1-00b0-4d18-be8a-30bd2d5a9350): No description
- `hasexternals` (ID: 1d54d4ea-6463-4d0a-9959-ef9ba149dcbc): No description
- `hascommon` (ID: 240ade37-1f44-4ad7-a2bd-0cb6be13a3c1): No description
- `hascallstatement` (ID: 68ecc6d7-3acc-49f3-beae-1fb8acf75caf): No description
- `hasbody` (ID: 429b7f43-4c2a-46ff-9764-7229edf65aa4): No description
- `getusercode1` (ID: 908a1ebf-efa5-4ff2-8b39-ff4a9a706246): No description
- `getusercode` (ID: 129799a2-3a8c-45ae-ab43-e0d78d8230a1): No description
- `getuseblocks` (ID: bea0d4e3-5fca-4a72-99ff-696e4be69023): No description
- `getrestdoc` (ID: 6d0d7a0a-778b-41fc-a3c9-1734115a13e5): No description
- `getpymethoddef` (ID: f4755d5c-d24c-4828-ac48-f5befece6fcd): No description
- `getfortranname` (ID: e2d73f26-f4da-4e95-89b7-33589ba87b8b): No description
- `getdimension` (ID: f3a1cc9a-07d4-44fa-b7dd-4a4ca206e05f): No description
- `getcallstatement` (ID: efac234f-e24f-43fc-9741-3af74fe54716): No description
- `getcallprotoargument` (ID: b83cc238-a16f-4f45-b2b4-2c944d02bf19): No description
- `getargs2` (ID: 1a0d9927-bd1c-4c9a-ab80-ed16b68ca957): No description
- `get_f2py_modulename` (ID: f98e4b01-dea3-4a2f-ad9e-9d9b1111701e): No description
- `gentitle` (ID: 4eee57df-f648-427c-ae19-44073b02ba88): No description
- `dictappend` (ID: eef515e9-b792-4bcf-855e-04387a4fc1f6): No description
- `debugcapi` (ID: 7cb081e2-8283-43fd-af2c-c1497d7749ff): No description
- `containsderivedtypes` (ID: f7b7ce8b-e8e6-4686-a98f-dd30f952a845): No description
- `containscommon` (ID: 7feaed81-5ce5-4c05-b3c1-a0078e598573): No description
- `applyrules` (ID: 6b197358-c412-4a1b-80a0-e9e52de57001): No description
- `UnixCCompiler_create_static_lib` (ID: a38f8af3-2f55-4469-be23-42493189a848): Build a static library in a separate sub-process.

Parameters
----------
objects : list or tuple of str
    List of paths to object files used to build the static library.
output_libname : str
    The library name as an absolute or relative (if `output_dir` is used)
    path.
output_dir : str, optional
    The path to the output directory. Default is None, in which case
    the ``output_dir`` attribute of the UnixCCompiler instance.
debug : bool, optional
    This parameter is not used.
target_lang : str, optional
    This parameter is not used.

Returns
-------
None
- `UnixCCompiler__compile` (ID: 456660ff-7607-4c51-bfb1-5b990fd43cc9): Compile a single source files with a Unix-style compiler.
- `has_f90_compiler` (ID: f4240685-9504-4e95-bdf5-1212fdf6f149): No description
- `has_f77_compiler` (ID: 08879a21-8748-4f14-b7f2-9977e558896f): No description
- `has_c_compiler` (ID: 44f99b5c-f864-4b64-a51d-7654b6e8d455): No description
- `test_distutils_parse_env_order` (ID: 6cd49059-b386-4bf7-86e7-b1b2de40716d): No description
- `have_compiler` (ID: e10a3340-9660-40e2-8f5e-8cd025d8f1bc): Return True if there appears to be an executable compiler
- `get_class` (ID: 11e96361-0b72-4902-ae45-50749fb5477a): notfound_action:
  0 - do nothing
  1 - display warning message
  2 - raise error
- `test_roundtrip` (ID: 7b4a7988-b1b8-47e5-8e38-3eed7a0f456c): Test that split is the inverse operation of join
- `test_join_matches_subprocess` (ID: fe5058c8-cee6-4ffd-ac27-1c0b0104c86b): Test that join produces strings understood by subprocess
- `runner` (ID: 9f07b27f-6fa3-43d8-99cb-6aa57782ddeb): No description
- `Parser` (ID: da3d6775-f065-4367-b176-4b045d5040f3): No description
- `test_installed_npymath_ini` (ID: 752e48d3-d16a-4eb5-b9b1-77e0182fc5a8): No description
- `test_build_import` (ID: 05ed1d46-efeb-4ba8-978e-b187f4750f82): Test the mingw32ccompiler.build_import_library, which builds a
`python.a` from the MSVC `python.lib`
- `test_log_prefix` (ID: 885178bc-59e3-41e8-8c64-c6fa4c021172): No description
- `teardown_module` (ID: 76fb7c83-c21a-4928-8680-d78a01505325): No description
- `setup_module` (ID: 1a24fb60-910c-4def-940d-fe1d9b51f861): No description
- `test_from_template` (ID: bb4d9fe8-42cf-48f8-9cfa-1178852340d0): Regression test for gh-10712.
- `normalize_whitespace` (ID: 1bcfc041-d3d5-47e3-b5b3-5a801dda4bed): Remove leading and trailing whitespace, and convert internal
stretches of whitespace to a single space.
- `test_fcompiler_flags` (ID: 2c838148-a1e5-4e6f-b752-8acf11b6491e): No description
- `test_exec_command_stdout` (ID: 7090ef9b-52af-4a37-a9f8-f35cf884b4f9): No description
- `test_exec_command_stderr` (ID: 16adafc9-e18e-470e-9285-032c03feb190): No description
- `new_test` (ID: ef5d4a77-91ec-48df-b400-b10c69578608): No description
- `test_multi_fortran_libs_link` (ID: c8984f03-1073-49ce-a7ed-493d33d85eeb): Ensures multiple "fake" static libraries are correctly linked.
see gh-18295
- `read_config` (ID: 624cfee3-bdf9-4f39-844f-d335692d72d0): Return library info for a package from its configuration file.

Parameters
----------
pkgname : str
    Name of the package (should match the name of the .ini file, without
    the extension, e.g. foo for the file foo.ini).
dirs : sequence, optional
    If given, should be a sequence of directories - usually including
    the NumPy base directory - where to look for npy-pkg-config files.

Returns
-------
pkginfo : class instance
    The `LibraryInfo` instance containing the build information.

Raises
------
PkgNotFound
    If the package is not found.

See Also
--------
misc_util.get_info, misc_util.get_pkg_info

Examples
--------
>>> npymath_info = np.distutils.npy_pkg_config.read_config('npymath')
>>> type(npymath_info)
<class 'numpy.distutils.npy_pkg_config.LibraryInfo'>
>>> print(npymath_info)
Name: npymath
Description: Portable, core math library implementing C99 standard
Requires:
Version: 0.1  #random
- `parse_flags` (ID: c3735d86-07a9-49c9-8a83-907994a88718): Parse a line from a config file containing compile flags.

Parameters
----------
line : str
    A single line containing one or more compile flags.

Returns
-------
d : dict
    Dictionary of parsed flags, split into relevant categories.
    These categories are the keys of `d`:

    * 'include_dirs'
    * 'library_dirs'
    * 'libraries'
    * 'macros'
    * 'ignored'
- `lib_opts_if_msvc` (ID: 2eb86176-c622-4322-814d-8a17d06dc828): Add flags if we are using MSVC compiler

We can't see `build_cmd` in our scope, because we have not initialized
the distutils build command, so use this deferred calculation to run
when we are building the library.
- `yellow_text` (ID: 558c4d38-a0c0-4adc-9e1d-f64d5022669d): No description
- `terminal_has_colors` (ID: a7bf159f-bd53-40d8-8110-3b13cd58a61c): No description
- `sanitize_cxx_flags` (ID: 40a2715b-3721-456c-a15b-1fccb599adfc): Some flags are valid for C but not C++. Prune them.
- `red_text` (ID: 2c598c01-16a8-41db-887b-c0ff8185b9f8): No description
- `njoin` (ID: fb4fa0f5-5065-4b93-81dc-72321d904144): Join two or more pathname components +
- convert a /-separated pathname to one using the OS's path separator.
- resolve `..` and `.` from path.

Either passing n arguments as in njoin('a','b'), or a sequence
of n names as in njoin(['a','b']) is handled, or a mixture of such arguments.
- `minrelpath` (ID: ab0ae94b-c136-4662-88a1-2c06ab6f8ea8): Resolve `..` and '.' from path.
- `mingw32` (ID: e59db6c4-90b4-401c-8b83-df8c3e7bbb86): Return true when using mingw32 environment.
- `is_string` (ID: 6620f017-ce14-4046-9cb1-dfe17f4d4446): No description
- `is_sequence` (ID: 1f52a922-88bc-4259-83a8-0f02ad4d3595): No description
- `is_local_src_dir` (ID: 01aee921-fd76-4e18-9518-a26b883690ba): Return true if directory is local directory.
- `has_f_sources` (ID: 0a2764d1-bfa3-420e-bfa3-c6e802c74315): Return True if sources contains Fortran files
- `has_cxx_sources` (ID: 3026c485-f9da-4bb3-9e28-696501cd3cf2): Return True if sources contains C++ files
- `green_text` (ID: db886c07-8a54-4b2d-8a53-ab0d8c16daad): No description
- `gpaths` (ID: 68a6f4b5-0b8e-4a52-ac88-3b06afc3feda): Apply glob to paths and prepend local_path if needed.
- `get_script_files` (ID: 6b672c37-8b0a-43c5-b802-80fc474b12a0): No description
- `get_pkg_info` (ID: 3c343609-385e-45ce-8081-e1b665dc1567): Return library info for the given package.

Parameters
----------
pkgname : str
    Name of the package (should match the name of the .ini file, without
    the extension, e.g. foo for the file foo.ini).
dirs : sequence, optional
    If given, should be a sequence of additional directories where to look
    for npy-pkg-config files. Those directories are searched prior to the
    NumPy directory.

Returns
-------
pkginfo : class instance
    The `LibraryInfo` instance containing the build information.

Raises
------
PkgNotFound
    If the package is not found.

See Also
--------
Configuration.add_npy_pkg_config, Configuration.add_installed_library,
get_info
- `get_numpy_include_dirs` (ID: a654be5d-326c-46a4-bbd2-9f9ad48af0ac): No description
- `get_num_build_jobs` (ID: aae7b0b8-af47-4d2e-a75b-967f813b2381): Get number of parallel build jobs set by the --parallel command line
argument of setup.py
If the command did not receive a setting the environment variable
NPY_NUM_BUILD_JOBS is checked. If that is unset, return the number of
processors on the system, with a maximum of 8 (to prevent
overloading the system if there a lot of CPUs).

Returns
-------
out : int
    number of parallel jobs that can be run
- `get_mathlibs` (ID: 5edc7492-9998-48c5-9983-33ca00a12cb8): Return the MATHLIB line from numpyconfig.h
- `get_lib_source_files` (ID: 01e3b765-fb2f-496b-bcf9-3d21dce0ac1d): No description
- `get_language` (ID: cfea0d8e-7e41-45d2-bdb1-ca39b13a1c1f): Determine language value (c,f77,f90) from sources
- `get_info` (ID: a377e4e1-1f41-41bd-9e67-3a78ff73242d): Return an info dict for a given C library.

The info dict contains the necessary options to use the C library.

Parameters
----------
pkgname : str
    Name of the package (should match the name of the .ini file, without
    the extension, e.g. foo for the file foo.ini).
dirs : sequence, optional
    If given, should be a sequence of additional directories where to look
    for npy-pkg-config files. Those directories are searched prior to the
    NumPy directory.

Returns
-------
info : dict
    The dictionary with build information.

Raises
------
PkgNotFound
    If the package is not found.

See Also
--------
Configuration.add_npy_pkg_config, Configuration.add_installed_library,
get_pkg_info

Examples
--------
To get the necessary information for the npymath library from NumPy:

>>> npymath_info = np.distutils.misc_util.get_info('npymath')
>>> npymath_info                                    #doctest: +SKIP
{'define_macros': [], 'libraries': ['npymath'], 'library_dirs':
['.../numpy/_core/lib'], 'include_dirs': ['.../numpy/_core/include']}

This info dict can then be used as input to a `Configuration` instance::

  config.add_extension('foo', sources=['foo.c'], extra_info=npymath_info)
- `get_frame` (ID: ea221348-c5b7-43f9-b738-a96544233f6c): Return frame object from call stack with given level.
- `get_ext_source_files` (ID: b88d44e2-ef71-4b41-a4c6-cc3354029104): No description
- `get_dependencies` (ID: 4fa18890-5ae0-4429-b39b-3a4f694f8124): No description
- `get_data_files` (ID: a8ef610f-7b37-420b-8f9a-cd5514e0b6b3): No description
- `get_cmd` (ID: d228a193-73e6-4828-9e63-094490cfc491): No description
- `get_build_architecture` (ID: a6d2df63-6947-474c-853a-5164a2c808f2): No description
- `generate_config_py` (ID: 11c63095-c02a-4663-a666-dece6a8c50b4): Generate config.py file containing system_info information
used during building the package.

Usage:
    config['py_modules'].append((packagename, '__config__',generate_config_py))
- `filter_sources` (ID: 8eed8f84-28a3-46c6-9bba-54977652b2fb): Return four lists of filenames containing
C, C++, Fortran, and Fortran 90 module sources,
respectively.
- `exec_mod_from_location` (ID: b3db7e94-b65e-4dd5-8bc7-43e4341c01f1): Use importlib machinery to import a module `modname` from the file
`modfile`. Depending on the `spec.loader`, the module may not be
registered in sys.modules.
- `dot_join` (ID: 0ac390f0-2ddd-4537-9f95-25413939d413): No description
- `dict_append` (ID: 4988b8c3-75d0-4e22-9e11-55464f82a56c): No description
- `default_config_dict` (ID: 296498ed-74c2-45ab-8d20-9abbc89fde87): Return a configuration dictionary for usage in
configuration() function defined in file setup_<name>.py.
- `cyg2win32` (ID: 81b7cbb5-e2db-4c73-88ac-f977c1f913e9): Convert a path from Cygwin-native to Windows-native.

Uses the cygpath utility (part of the Base install) to do the
actual conversion.  Falls back to returning the original path if
this fails.

Handles the default ``/cygdrive`` mount prefix as well as the
``/proc/cygdrive`` portable prefix, custom cygdrive prefixes such
as ``/`` or ``/mnt``, and absolute paths such as ``/usr/src/`` or
``/home/username``

Parameters
----------
path : str
   The path to convert

Returns
-------
converted_path : str
    The converted path

Notes
-----
Documentation for cygpath utility:
https://cygwin.com/cygwin-ug-net/cygpath.html
Documentation for the C function it wraps:
https://cygwin.com/cygwin-api/func-cygwin-conv-path.html
- `cyan_text` (ID: 436e0804-1bd7-455f-ac00-089106938a14): No description
- `blue_text` (ID: 6c95ca3a-0a04-4747-bc28-27fe239a12e2): No description
- `as_list` (ID: 461da794-42e5-4b7a-b181-d206c3d6eca3): No description
- `appendpath` (ID: 92a5d9fa-72cf-4619-a684-728d263d3d5e): No description
- `allpath` (ID: fcc5b705-bbae-472f-acfa-0ed7957d6993): Convert a /-separated pathname to one using the OS's path separator.
- `all_strings` (ID: e080f750-ad4a-4f64-a493-be10dd0cfa4f): Return True if all items in lst are string objects.
- `rc_name` (ID: f951b651-b448-472f-96b5-0b75bbf2e25d): No description
- `msvc_manifest_xml` (ID: 8325bbc1-3803-4882-8a74-dfa75d34de89): Given a major and minor version of the MSVCR, returns the
corresponding XML file.
- `manifest_rc` (ID: b2b77932-1e5f-4281-a704-2683df197348): Return the rc file used to generate the res file which will be embedded
as manifest for given manifest file name, of given type ('dll' or
'exe').

Parameters
----------
name : str
        name of the manifest file to embed
type : str {'dll', 'exe'}
        type of the binary which will embed the manifest
- `manifest_name` (ID: 40d32af3-26c0-471d-afa5-9b4566900905): No description
- `get_msvcr_replacement` (ID: f8735b69-29db-4552-bf00-207240b90ff2): Replacement for outdated version of get_msvcr from cygwinccompiler
- `generate_manifest` (ID: a2eeb6a0-8950-460b-ae53-d75e3f8718d8): No description
- `generate_def` (ID: c656f57d-15ca-45b4-831d-2da450864396): Given a dll file location,  get all its exported symbols and dump them
into the given def file.

The .def file will be overwritten
- `find_python_dll` (ID: 38b01d57-5864-444d-8bc3-9bb11e5b2c5d): No description
- `find_dll` (ID: c795e957-702c-490b-b428-e74ec14833b7): No description
- `dump_table` (ID: c98f69fa-b563-4090-8083-1022da8edd9f): No description
- `configtest_name` (ID: 8c06e40f-8051-460d-9c69-c3537071c9bf): No description
- `check_embedded_msvcr_match_linked` (ID: d99a7e71-f1ed-4d77-89eb-e3e1a2c992d1): msver is the ms runtime version used for the MANIFEST.
- `build_msvcr_library` (ID: 7fb1bc5b-7e78-490a-92e2-cd9c7f01ddea): No description
- `build_import_library` (ID: 4bc4af0f-6134-4463-85ea-6004dd9c523d): No description
- `warn` (ID: 1263dd98-b4cd-42e0-a97a-b1987045fc6b): No description
- `set_verbosity` (ID: 0f7cd5ac-ec9b-4cab-a33e-918c82b3cb21): No description
- `set_threshold` (ID: 5cb8bd7b-b24e-40a7-9bc3-372126a62ec2): No description
- `info` (ID: 672f40c6-c0d1-4a9c-b705-181651ec3dfb): No description
- `get_threshold` (ID: 3fc6be97-24fb-4528-8128-0ef1748e37b4): No description
- `error` (ID: 139fb3f7-5dcd-4876-b1ec-69e7b98d4f9b): No description
- `debug` (ID: 2804688d-40b8-4cc8-8157-cf139317e527): No description
- `unix2dos_one_dir` (ID: 7ea817e6-2d57-4cc6-9f8d-ed110cc22027): No description
- `unix2dos_dir` (ID: a0b8b290-f86d-481f-b6ab-f2a07a79a134): No description
- `unix2dos` (ID: 82e1cbca-f798-4207-bfa1-9b126c80fdc3): Replace LF with CRLF in argument files.  Print names of changed files.
- `dos2unix_one_dir` (ID: e974b6fa-3360-4aa5-afcc-b8b34b357880): No description
- `dos2unix_dir` (ID: 34a7d08a-3d8e-4c01-86a6-002b60797e8b): No description
- `dos2unix` (ID: 1d65e1c8-1be3-45fd-85b6-1d28011d8809): Replace CRLF with LF in argument files.  Print names of changed files.
- `parse_nm` (ID: 77eee592-b0a6-4801-b820-72913bb9eac5): Returns a tuple of lists: dlist for the list of data
symbols and flist for the list of function symbols.

dlist, flist = parse_nm(nm_output)
- `parse_cmd` (ID: c19b53a8-89fa-4854-b39d-cba443e020f3): Parses the command-line arguments.

libfile, deffile = parse_cmd()
- `output_def` (ID: 45015e2d-4cce-46f1-87d6-3c9dd96d4485): Outputs the final DEF file to a file defaulting to stdout.

output_def(dlist, flist, header, file = sys.stdout)
- `getnm` (ID: 959ca74f-9b18-4eda-97cc-0f425120af46): Returns the output of nm_cmd via a pipe.

nm_output = getnm(nm_cmd = 'nm -Cs py_lib')
- `process_str` (ID: c0273907-8afe-4371-b3ea-63a9b06d2113): No description
- `process_file` (ID: 3228c84a-1f7a-43d2-bd38-44d89912ae52): No description
- `show_fcompilers` (ID: f408589e-7ed4-4fc4-a296-e1fcfaf8b7c9): Print list of available compilers (used by the "--help-fcompiler"
option to "config_fc").
- `new_fcompiler` (ID: 904cec4e-eb98-4236-a50a-bef9b0ebdb40): Generate an instance of some FCompiler subclass for the supplied
platform/compiler combination.
- `intel_version_match` (ID: fb379e15-99fe-4661-9763-282c87a9c2cf): No description
- `is_win64` (ID: 484adc7f-548b-4eee-b68a-4d8e00fc35ac): No description
- `dummy_fortran_file` (ID: 06d3a259-2ea3-422b-9eb4-9dbf6a06f4a4): No description
- `find_executable` (ID: 0d4f2cf5-3abf-434b-a47d-0835f1a8af7c): Return full path of a executable or None.

Symbolic links are not followed.
- `exec_command` (ID: 45e6b90e-d8ec-41a8-86f1-920bf179354c): Return (status,output) of executed command.

.. deprecated:: 1.17
    Use subprocess.Popen instead

Parameters
----------
command : str
    A concatenated string of executable and arguments.
execute_in : str
    Before running command ``cd execute_in`` and after ``cd -``.
use_shell : {bool, None}, optional
    If True, execute ``sh -c command``. Default None (True)
use_tee : {bool, None}, optional
    If True use tee. Default None (True)


Returns
-------
res : str
    Both stdout and stderr messages.

Notes
-----
On NT, DOS systems the returned status is correct for external commands.
Wild cards will not work for non-posix systems or when use_shell=0.
- `customized_fcompiler` (ID: 994bd49a-bfd2-41b0-be62-f1fa00e61143): No description
- `customized_ccompiler` (ID: a2396bf0-b871-4c12-8598-4ca1936dac13): No description
- `setup` (ID: 48e0d361-d5ce-495c-9672-7e9893c3345f): No description
- `get_distribution` (ID: 441057b6-9f34-436d-8c90-b321f3998ee2): No description
- `process_str` (ID: e81e6a86-c0b3-490d-9910-83bc31b6ed2f): No description
- `process_file` (ID: a7a3c331-99b1-4241-b9f7-8f00190c5416): No description
- `show_fortran_compilers` (ID: b0a50a82-d20f-4309-8710-6e27e6947c71): No description
- `subst_vars` (ID: faf4a755-2d22-47e1-80b3-53c664cf0d09): Substitute any occurrence of @foo@ by d['foo'] from source file into
target.
- `get_swig_target` (ID: 14f57e9c-715b-47ed-ab5a-4462dd2c6281): No description
- `get_swig_modulename` (ID: 93bb7c18-814b-4c61-9598-70ded768f364): No description
- `get_f2py_modulename` (ID: ddae206a-8ffa-482c-841d-86c33ca7c0ef): No description
- `check_restrict` (ID: 37868446-770b-421a-92c3-8172f400952f): Return the restrict identifier (may be empty).
- `check_inline` (ID: 59eef7b3-3a8e-4653-bba8-6b14f93bf5b5): Return the inline identifier (may be empty).
- `check_gcc_version_at_least` (ID: ecb0727a-b7f5-4430-a056-af18d93ecc3d): Check that the gcc version is at least the specified version.
- `check_gcc_variable_attribute` (ID: 7ee7bdde-d772-4379-845b-08d280feeb02): Return True if the given variable attribute is supported.
- `check_gcc_function_attribute_with_intrinsics` (ID: 3bda74ca-3595-43b2-844e-13871a4999f1): Return True if the given function attribute is supported with
intrinsics.
- `check_gcc_function_attribute` (ID: 25073d7c-cf2c-4bf3-a31a-4f687b95f36b): Return True if the given function attribute is supported.
- `check_compiler_gcc` (ID: 41515d49-a224-43b9-a1c5-599f4e5bbef6): Check if the compiler is GCC.
- `new_ccompiler_opt` (ID: ea63d9a3-cf1b-4efd-b6bd-3d6a9fc9b7a8): Create a new instance of 'CCompilerOpt' and generate the dispatch header
which contains the #definitions and headers of platform-specific instruction-sets for
the enabled CPU baseline and dispatch-able features.

Parameters
----------
compiler : CCompiler instance
dispatch_hpath : str
    path of the dispatch header

**kwargs: passed as-is to `CCompilerOpt(...)`
Returns
-------
new instance of CCompilerOpt
- `simple_version_match` (ID: f7c5f6f7-6d8d-4c0b-a4e7-46364b6f1589): Simple matching of version numbers, for use in CCompiler and FCompiler.

Parameters
----------
pat : str, optional
    A regular expression matching version numbers.
    Default is ``r'[-.\d]+'``.
ignore : str, optional
    A regular expression matching patterns to skip.
    Default is ``''``, in which case nothing is skipped.
start : str, optional
    A regular expression matching the start of where to start looking
    for version numbers.
    Default is ``''``, in which case searching is started at the
    beginning of the version string given to `matcher`.

Returns
-------
matcher : callable
    A function that is appropriate to use as the ``.version_match``
    attribute of a ``distutils.ccompiler.CCompiler`` class. `matcher` takes a single parameter,
    a version string.
- `replace_method` (ID: 18ec1b4b-e0f1-4d76-9fe9-65ce3fce4989): No description
- `CCompiler_spawn` (ID: 948f90b2-06d8-4848-805d-a48a4cd07893): Execute a command in a sub-process.

Parameters
----------
cmd : str
    The command to execute.
display : str or sequence of str, optional
    The text to add to the log file kept by `numpy.distutils`.
    If not given, `display` is equal to `cmd`.
env : a dictionary for environment variables, optional

Returns
-------
None

Raises
------
DistutilsExecError
    If the command failed, i.e. the exit status was not 0.
- `CCompiler_show_customization` (ID: f84f578d-ab1e-44fc-a95e-adbd33fda504): Print the compiler customizations to stdout.

Parameters
----------
None

Returns
-------
None

Notes
-----
Printing is only done if the distutils log threshold is < 2.
- `CCompiler_object_filenames` (ID: 425b20bb-b845-4b6d-a419-e7466e5925d8): Return the name of the object files for the given source files.

Parameters
----------
source_filenames : list of str
    The list of paths to source files. Paths can be either relative or
    absolute, this is handled transparently.
strip_dir : bool, optional
    Whether to strip the directory from the returned paths. If True,
    the file name prepended by `output_dir` is returned. Default is False.
output_dir : str, optional
    If given, this path is prepended to the returned paths to the
    object files.

Returns
-------
obj_names : list of str
    The list of paths to the object files corresponding to the source
    files in `source_filenames`.
- `CCompiler_get_version` (ID: 0390c48f-0dff-45f5-8141-528d297cfeb3): Return compiler version, or None if compiler is not available.

Parameters
----------
force : bool, optional
    If True, force a new determination of the version, even if the
    compiler already has a version attribute. Default is False.
ok_status : list of int, optional
    The list of status values returned by the version look-up process
    for which a version string is returned. If the status value is not
    in `ok_status`, None is returned. Default is ``[0]``.

Returns
-------
version : str or None
    Version string, in the format of ``distutils.version.LooseVersion``.
- `CCompiler_find_executables` (ID: dba66c2d-3ef4-4031-a66d-f5b35b906484): Does nothing here, but is called by the get_version method and can be
overridden by subclasses. In particular it is redefined in the `FCompiler`
class where more documentation can be found.
- `CCompiler_cxx_compiler` (ID: 5d457475-83ec-49f6-a5b3-187c25c992cb): Return the C++ compiler.

Parameters
----------
None

Returns
-------
cxx : class instance
    The C++ compiler, as a ``distutils.ccompiler.CCompiler`` instance.
- `CCompiler_customize_cmd` (ID: d7cecc54-b04a-4f9d-ba11-05351a3a1382): Customize compiler using distutils command.

Parameters
----------
cmd : class instance
    An instance inheriting from ``distutils.cmd.Command``.
ignore : sequence of str, optional
    List of ``distutils.ccompiler.CCompiler`` commands (without ``'set_'``) that should not be
    altered. Strings that are checked for are:
    ``('include_dirs', 'define', 'undef', 'libraries', 'library_dirs',
    'rpath', 'link_objects')``.

Returns
-------
None
- `CCompiler_customize` (ID: 7929d2b6-b260-4d21-a39e-026fd4232431): Do any platform-specific customization of a compiler instance.

This method calls ``distutils.sysconfig.customize_compiler`` for
platform-specific customization, as well as optionally remove a flag
to suppress spurious warnings in case C++ code is being compiled.

Parameters
----------
dist : object
    This parameter is not used for anything.
need_cxx : bool, optional
    Whether or not C++ has to be compiled. If so (True), the
    ``"-Wstrict-prototypes"`` option is removed to prevent spurious
    warnings. Default is False.

Returns
-------
None

Notes
-----
All the default options used by distutils can be extracted with::

  from distutils import sysconfig
  sysconfig.get_config_vars('CC', 'CXX', 'OPT', 'BASECFLAGS',
                            'CCSHARED', 'LDSHARED', 'SO')
- `CCompiler_compile` (ID: af0e4ce4-38f1-45a8-820b-b3098a71cfaf): Compile one or more source files.

Please refer to the Python distutils API reference for more details.

Parameters
----------
sources : list of str
    A list of filenames
output_dir : str, optional
    Path to the output directory.
macros : list of tuples
    A list of macro definitions.
include_dirs : list of str, optional
    The directories to add to the default include file search path for
    this compilation only.
debug : bool, optional
    Whether or not to output debug symbols in or alongside the object
    file(s).
extra_preargs, extra_postargs : ?
    Extra pre- and post-arguments.
depends : list of str, optional
    A list of file names that all targets depend on.

Returns
-------
objects : list of str
    A list of object file names, one per source file `sources`.

Raises
------
CompileError
    If compilation fails.
- `__getattr__` (ID: c9da1a1f-a85b-4cce-95d2-54e9aa501c9c): No description
- `__getattr__` (ID: e0e21ae1-97c2-43f0-b818-a6d6992098f6): No description
- `__getattr__` (ID: f53fe430-4d96-413d-abc8-6f38841145d4): No description
- `__getattr__` (ID: f0305182-ee2e-4e72-9cf4-5a80eb414d5e): No description
- `__getattr__` (ID: 72ef33d6-f72c-44b7-b6af-52e83fe33913): No description
- `__getattr__` (ID: 1f0b4875-537a-4474-bd3e-da560a7f1513): No description
- `__getattr__` (ID: df084493-c955-453f-bc8f-69b7f9a03ae1): No description
- `__getattr__` (ID: e3d9cbec-5a5e-48be-b0bb-cfda0683f8bc): No description
- `__getattr__` (ID: 28d5e57a-916b-46c6-8122-b71562fe73f9): No description
- `__getattr__` (ID: 7a74a18a-a866-476f-98f1-5a00c73dcf7f): No description
- `__getattr__` (ID: d7978af3-49cd-466f-acc5-2cef3ff6efe5): No description
- `__getattr__` (ID: 87ffb3e0-4b40-4cc8-9c2c-07769597d436): No description
- `__getattr__` (ID: 03232ac3-6074-4082-a12d-514874a00dd6): No description
- `__getattr__` (ID: 46d065a5-6533-4460-aecb-fa6ae43fc11a): No description
- `__getattr__` (ID: 838bba69-b157-45e4-929c-2e64584ec98d): No description
- `__getattr__` (ID: c947671c-1f1d-4d83-abe1-14e0e3f03c41): No description
- `__getattr__` (ID: 80f437a5-c5ac-457c-99a3-2a89b537a918): No description
- `__getattr__` (ID: 07f4989e-5de1-4d24-979a-bf7e5681aaea): No description
- `warnings_errors_and_rng` (ID: dcc159f0-9d13-4c7f-a159-43e701690c77): Filter out the wall of DeprecationWarnings.
- `random_string_list` (ID: a3aff021-ef98-460a-8dc5-b194c0c90380): No description
- `pytest_terminal_summary` (ID: cc4662b1-399d-4aae-98b0-5b0f7f165f1c): No description
- `pytest_sessionstart` (ID: 7a18e4de-3857-4283-877d-f4af89556842): No description
- `pytest_itemcollected` (ID: 1d9c8346-0253-43d1-b895-5b4460c92300): Check FPU precision mode was not changed during test collection.

The clumsy way we do it here is mainly necessary because numpy
still uses yield tests, which can execute code at test collection
time.
- `pytest_configure` (ID: ffe729cd-9eb2-4ce2-881d-339c8673ee3b): No description
- `pytest_addoption` (ID: 3032d30f-bd61-45bf-9b47-c11980aa35b9): No description
- `na_object` (ID: 5046761e-a47e-4715-8a75-4cdc7b940762): No description
- `env_setup` (ID: 5fa8c14c-6319-4d8f-b8d7-595a55611a42): No description
- `dtype` (ID: ac60494c-f12a-4442-a0fb-e724f5c76104): No description
- `coerce` (ID: 5cfa5500-ab69-454b-9721-dd04a0ced2ab): No description
- `check_fpu_mode` (ID: 751a3699-f622-47b6-b21e-161c90eccfc5): Check FPU precision mode was not changed during the test.
- `add_np` (ID: 310c39ee-29ce-4fe1-a00e-9721ca97f8ee): No description
- `write_release_task` (ID: e7e6ea0c-4239-4e58-b18e-08922a213628): Append hashes of release files to release notes.

This appends file hashes to the release notes and creates
four README files of the result in various formats:

- README.rst
- README.rst.gpg
- README.md
- README.md.gpg

The md file are created using `pandoc` so that the links are
properly updated. The gpg files are kept separate, so that
the unsigned files may be edited before signing if needed.

Parameters
----------
options :
    Set by ``task`` decorator.
filename : str
    Filename of the modified notes. The file is written
    in the release directory.
- `write_release` (ID: 7e662717-63ea-47b9-b89a-79077908ae67): Write the README files.

Two README files are generated from the release notes, one in ``rst``
markup for the general release, the other in ``md`` markup for the github
release notes.

Parameters
----------
options :
    Set by ``task`` decorator.
- `compute_sha256` (ID: 6609d1f0-d4ca-49b4-91b9-d09a88d707b8): Compute sha256 hash of files in idirs.

Parameters
----------
idirs : directory path
    Directory containing files to be hashed.
- `compute_md5` (ID: 7918b583-930f-4573-b170-6ab7240f6eb1): Compute md5 hash of files in idirs.

Parameters
----------
idirs : directory path
    Directory containing files to be hashed.

## Running the Service

### Local Development
```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### Docker
```bash
docker build -t numpy-api .
docker run -p 8080:8080 numpy-api
```

## API Endpoints

- `GET /health` - Health check
- `GET /docs` - Interactive API documentation
- `POST /{function_name_or_id}` - Individual function endpoints
- `POST /batch` - Batch execution of multiple functions

## Performance Features

This API uses **orjson** for JSON serialization, which provides:
- 2-3x faster JSON serialization compared to standard library
- Better handling of datetime objects, UUIDs, and other Python types
- Automatic optimization for large payloads
- Lower memory usage

## Example Usage

```python
import requests

# Call individual function
response = requests.post("http://localhost:8080/41aad374-b32e-4fb8-a908-ca3af446b356", 
                        json={"param1": "value1", "param2": "value2"})
print(response.json())

# Batch execution
batch_response = requests.post("http://localhost:8080/batch", 
                              json=[
                                  {"function_id": "41aad374-b32e-4fb8-a908-ca3af446b356", "param1": "value1"},
                                  {"function_id": "5db9858d-dfbf-4d24-a6e4-5276cfeed96e", "param2": "value2"}
                              ])
print(batch_response.json())
```

## Response Format

All endpoints return responses in the following format:
```json
{
    "success": true,
    "result": {"your": "data"},
    "error": null,
    "function_id": "function-id",
    "function_name": "function_name"
}
```

In case of errors:
```json
{
    "success": false,
    "result": null,
    "error": "Error description with traceback",
    "function_id": "function-id",
    "function_name": "function_name"
}
```
