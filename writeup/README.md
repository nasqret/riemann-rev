# The condensed Lean proof of RH and GRH: a reading (working draft)

A complete reading, as mathematics, of the Lean proof in
[`lsernau/grh-lean`](https://github.com/lsernau/grh-lean), edition `grh-compact`, at commit
[`72fead1`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact): from the five
final theorems down through every unit of the argument, with classical results quoted from the literature.

> **Status.** The formal proof is a **claim**: its authors report that Lean's kernel accepts the five theorems with the
> three standard axioms. No mathematician has read the argument through, and **nothing here says that the Riemann
> hypothesis is proved**. This is a **working draft**, published early so that people and their agents can read, check
> and improve it. It has been read by AI agents and checked by programs, **not yet refereed by a human**. Every
> statement in it links to the exact Lean lines it renders, at the pinned commit.

## Start here

- **[`handout.pdf`](handout.pdf)**: the whole reading in one PDF. The overview of the argument (Theorems A, B, C and
  how they give GRH), then Chapters I–VIII in the order of the argument, the catalogue of quoted results and the
  record of checks. Every `LEAN` line under a statement is a link to the Lean source it renders.
- [`catalogue-full.pdf`](catalogue-full.pdf): every background result the argument uses, classified (definition,
  elementary lemma, named theorem, substantial result), with references and, for named theorems, how the formal
  statement compares with the published one.
- **For AI agents: [`AGENTS.md`](AGENTS.md)**: how this material is organised, how to verify any statement against
  the pinned Lean, and prompts for explaining, rewriting and checking it.

## What is here

| path | what |
|---|---|
| `handout.pdf` | overview, the notes in the order of the argument, condensed catalogue, record of checks |
| `catalogue-full.pdf` | the complete catalogue of quoted results |
| `overview.tex` | the overview's LaTeX source |
| `notes/<slug>/` | every note's LaTeX source (`<slug>.tex`, `data.tex`), its account of declarations (`spec.json`), its concordance with the Lean (`concordance.json`) and its reader index (`reader.json`) |
| `structured-proofs/<unit>/` | for every unit of the formal text: `unit.json` (every declaration, its statement in words, its arguments), `proofs/*.json` (each proof as a tree of small steps, each quoting the exact Lean lines it renders), `check.json` (the program check), `CORRECTIONS.md` (what the second reading changed) |
| `catalogue/` | the catalogue as JSON, and the second reader's comparison of each named theorem with its published statement |
| `MANIFEST.json` | the pin, the edition, the counts, and the SHA-256 of every file |

## How it was made, and what that does and does not check

1. **Structured proofs** (AI readers, Claude Opus 5.5): every declaration of the argument given a statement in words
   and every proof a tree of steps, each step quoting the exact Lean lines it renders. A program
   (the Readback method's `rb.py check`) compares every quotation, line range and hash with
   the source at the pinned commit, and accounts for every argument of every declaration. *This checks that the steps
   quote the right lines; it does not check that the English is right.*
2. **Second reading** (an independent AI reader): the statements and a sample of the steps re-read against
   the Lean; every named theorem of the background compared with its published statement, at a located place. Its
   corrections are applied (`CORRECTIONS.md` of each unit).
3. **Notes** (AI writers, Claude Fable 5.2): each unit rewritten as mathematics from its structured proofs, every
   statement compared with its Lean text; a build refuses a note that drops an argument or a hypothesis of a formal
   declaration. Each note says in its last sections what was read and what is taken for granted.
4. **Referees** (independent AI readers, Claude Opus 5.5): notes read as a referee reads a paper; their reports are being
   applied chapter by chapter.
5. **Not yet done**: a human referee's reading; an independent kernel build of this edition (interrupted by a cluster's
   scheduled downtime, to resume); Lean's own list of the arguments of every declaration compared with the readings
   (several are derived by hand and marked so).

## Licence and credit

Our text is under the repository's licence (0BSD). Quotations of Lean code are from
[`lsernau/grh-lean`](https://github.com/lsernau/grh-lean) (Apache License 2.0); the proof is Levent Alpöge's, with
Claude; the condensed edition is by Luke Sernau, colleagues at Anthropic, and Claude. Corrections are welcome as issues
of this repository: cite the note and the Lean lines.
