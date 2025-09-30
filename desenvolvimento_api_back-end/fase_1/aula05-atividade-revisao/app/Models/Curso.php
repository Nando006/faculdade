<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Curso extends Model
{
    protected $fillable = [
        'titulo',
        'descricao'
    ];

    public function matriculas(): HasMany {
        return $this->hasMany(Matricula::class);
    }
}
