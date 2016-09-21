test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '18f4b8f373a149983a060187fb945841',
          'choices': [
            'a list of restaurants reviewed by the user',
            'a list of all possible restaurants',
            'a list of ratings for restaurants reviewed by the user'
          ],
          'hidden': False,
          'locked': True,
          'question': 'In best_predictor, what does the variable reviewed represent?'
        },
        {
          'answer': '6e952a03cc93ab2e76cc6e9be1f58c8e',
          'choices': [
            'a predictor function, and its r_squared value',
            'a predictor function',
            'an r_squared value',
            'a restaurant'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Given a user, a list of restaurants, and a feature function, what
          does find_predictor from Problem 7 return?
          """
        },
        {
          'answer': '6290d50f08bc68e242b1124b49a5e8db',
          'choices': [
            'the predictor with the highest r_squared',
            'the predictor with the lowest r_squared',
            'the first predictor in the list',
            'an arbitrary predictor'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          After getting a list of [predictor, r_squared] pairs,
          which predictor should we select?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 2, [
          ...         make_review('D', 3),
          ...         make_review('D', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster] # should be a list of decimals
          [2.0, 5.0, 2.0, 5.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster]
          [2.0, 5.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
