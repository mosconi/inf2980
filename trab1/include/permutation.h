#ifndef __PERMUTATION_H__
#define __PERMUTATION_H__

typedef struct permutation_t permutation_t;

permutation_t *
permutation_new_empty(size_t sz);

permutation_t *
permutation_new(size_t sz);

void
permutation_destroy(permutation_t **);

permutation_t *
permutation_compose(permutation_t *, permutation_t *);


#endif
