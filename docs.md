# Documentazione di Foggiascript

Questa è la documentazione

## Basi

Le varie istruzioni sono divise da un ritorno a capo o una virgola.

Un cancelletto o hashtag `#` denota l'inizio di un commento su singola riga.

```
print("Ciao") # Questo è un commento
```

Per commenti multilinea utilizzare `#[` e `]#`. Include supporto per commenti annidati così non ti incavoli quando commenti del codice con la struttura multilinea e c'è un'altro commento multilinea e quindi si impalla.

```
#[
    Questo è un commento
    su più linee
    #[
        Guarda che figo
    ]#
]#
```

## Tipi di dato

Per ora ci sono interi, float, e stringhe

### Interi

Gli interi sono scritti proprio come pensi siano scritti

### Float

I float sono proprio come te li aspetti, ma un intero letterale può essere seguito dalla lettera `f` per considerarli un float.

```
25f
```

### Stringhe

Le stringhe sono delimitati da doppie virgolette. Per ora puoi fare l'escape della doppia virgoletta o del backslash con il backslash.

## Funzioni

Chiamale come fai di solito. Ancora non le puoi creare te.

## Cose builtin

### `print(...)`

Stampa dei valori alla console.

### `JavaScript`

Accedi allo scope originario di JavaScript. Ad esempio puoi usare `JavaScript.prompt` come input semplice per il testing.