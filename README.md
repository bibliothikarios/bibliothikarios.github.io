# Βιβλιοθηκάριος

Ο [βιβλιοθηκάριος](https://bibliothikarios.github.io) είναι μια σελίδα που δίνει ελεύθερη πρόσβαση σε ηλεκτρονικά βιβλία (ebook).

## Βοήθεια

Για να προσθέσεις βιβλία:
- Ανέβασε το βιβλίο σου στο [IPFS](https://ipfs.io/).
- Πρόσθεσε στο αρχείο `resources.json` μια εγγραφή που περιέχει το IPFS ID και το όνομα του αρχείου του βιβλίου, στην κατάλληλη κατηγορία ανάλογα με τον τύπο του βιβλίου.
- Tρέξε το `create.py` για να δημιουργηθεί η ανανεωμένη σελίδα.

Για να κατεβάσεις τα αρχεία και να τα κάνεις seed, ώστε να είναι προσβάσιμα πιο γρήγορα για όλους:
- Τρέξε ένα IPFS node.
- Κάνε import τα αρχεία που επιθυμείς.
- Για κάθε κατηγορία υπάρχει ένα αντίστοιχο IPFS folder (βλ. `resources.json`), οπότε μπορείς να κάνεις import ολόκληρο το φάκελο για ευκολία.
- Κάνε `pin` τα αρχεία ή τους φακέλους, ώστε να αποθηκευτεί ένα αντίγραφο στον υπολογιστή σου και να μη διαγραφεί από το garbage collection του IPFS.

Εναλλακτικά, μπορείς να βοηθήσεις ως εξής:
- Πρόσθεσε features που θα ομορφύνουν ή/και θα κάνουν τη σελίδα πιο λειτουργική.
- Δημιούργησε έναν κλώνο της σελίδας, ώστε ακόμα και αν πέσει να υπάρχει διαθέσιμη αλλού.

## License

Ο κώδικας της σελίδας είναι [CC0](https://creativecommons.org/choose/zero/).
