# optparse — Adding new actions

### Adding new actions

Adding new actions runs a bit trickier, because you have to grasp that `optparse` keeps a couple of classifications for actions:

"store" actions

actions that make `optparse` write a value onto an attribute of the current OptionValues instance; such options need a `dest` attribute handed to the Option constructor.

"typed" actions

actions that pull a value off the command line and expect it to match a certain type; or more precisely, a string convertible into a certain type. Such options need a `type` attribute handed to the Option constructor.

These classifications overlap: among the default "store" actions are `"store"`, `"store_const"`, `"append"`, and `"count"`, whereas the default "typed" actions are `"store"`, `"append"`, and `"callback"`.

As you add an action, you must categorize it by listing it in at least one of the following Option class attributes (each is a list of strings):

 Option.ACTIONS

All actions must be listed in ACTIONS.

 Option.STORE_ACTIONS

"store" actions are additionally listed here.

 Option.TYPED_ACTIONS

"typed" actions are additionally listed here.

 Option.ALWAYS_TYPED_ACTIONS

Actions that invariably take a type (that is, whose options invariably take a value) get listed here as well. The sole consequence is that `optparse` hands the default type, `"string"`, to options lacking an explicit type whose action appears in `ALWAYS_TYPED_ACTIONS`.

To put your new action genuinely into effect, you have to override Option's `take_action()` method and insert a case that handles your action.

[Subject index](INDEX.md) · [Previous](option-types-to-option-type-checker.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Required continuation of the source contract](optparse-optionerror-to-optparse-ambiguousoptionerror.md)
