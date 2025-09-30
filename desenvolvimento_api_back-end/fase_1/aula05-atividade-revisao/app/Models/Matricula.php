<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Matricula extends Model
{
    protected $fillable = [
        'aluno_id',
        'curso_id'
    ];

    public function cursos(): BelongsToMany {
        return $this->belongsToMany(Curso::class);
    }

    public function aluno(): BelongsTo {
        return $this->belongsTo(Aluno::class);
    }
}
